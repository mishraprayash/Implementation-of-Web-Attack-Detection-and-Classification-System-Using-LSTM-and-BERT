# app/predictor.py

import time
import torch
from config import MODEL_PATH, VOCAB_PATH
from preprocessing import Preprocessor

# Define the labels corresponding to the model's output
LABELS = ['NORMAL', 'SQLI', 'XSS', 'CMDI', 'LFI', 'SSRF', 'HTMLI', 'CSSI', 'NOSQLI']

class Predictor:
    def __init__(self, model_path: str = MODEL_PATH, vocab_path: str = VOCAB_PATH):
        self.model = torch.jit.load(model_path, map_location="cpu")
        self.model.eval()  # Set model to evaluation mode
        self.preprocessor = Preprocessor(vocab_path)
    
    def predict(self, data: dict):
        start_time = time.time()
        processed = self.preprocessor.preprocess(data)
        model_input = torch.tensor(processed).unsqueeze(0)
        
        with torch.no_grad():
            output = self.model(model_input)
        
        inference_time = time.time() - start_time
        pred_index = torch.argmax(output, dim=1).item()
        pred = LABELS[pred_index]
        prediction_probability = torch.softmax(output, dim=1).max().item()
        
        # sends back these after prediction
        return {
            "prediction": pred,
            "inference_time_ms": round(inference_time * 1000, 6),
            "prediction_probability": round(prediction_probability,6)
        }
