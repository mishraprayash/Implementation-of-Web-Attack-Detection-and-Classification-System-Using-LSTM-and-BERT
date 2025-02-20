import uuid
import logging
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware

from schema import RequestData
from predictor import Predictor
from background_tasks import save_log_entry
from db import engine, Base, init_db

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Initialize database
init_db()
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize predictor instance
logger.info("📢 Loading model...")
predictor = Predictor()
logger.info("✅ Model loaded successfully.")

@app.post("/predict")
async def predict_endpoint(request: RequestData, background_tasks: BackgroundTasks):
    # converting to dict 
    data = request.model_dump()
    logger.info(f"🔍 Received request for prediction: {data['uri']}")

    try:
        result = predictor.predict(data)
        logger.info(f"✅ Prediction successful: {result['prediction']}")
    except Exception as e:
        logger.error(f"❌ Prediction failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    # Map the prediction to logging details
    pred = result["prediction"]
    prediction_probability = result["prediction_probability"]
    category = 'MALICIOUS' if pred != 'NORMAL' else 'NORMAL'
    attack_type = pred.upper() if pred != 'NORMAL' else 'NULL'
    severity = 'CRITICAL' if pred in ['SQLI', 'XSS', 'CMDI', 'LFI', 'SSRF'] else 'LOW'
    
    log_entry_data = {
        "id": str(uuid.uuid4()),
        "method": data['method'],  # Assuming the method is POST
        "endpoint": data["uri"],
        "ip": data["source_ip"],  # Replace with actual IP if available
        "category": category,
        "attackType": attack_type,
        "attackPayload": data["body"],
        "predictionProbability": prediction_probability,
        "severity": severity
    }
    
    # Schedule the database logging as a background task
    background_tasks.add_task(save_log_entry, log_entry_data)
    
    return result

@app.get('/health')
async def health_check():
    return {"status":"ok"}

