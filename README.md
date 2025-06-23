## Web Attack Detection & Classification System using LSTM and Mobile-BERT with FastAPI


This project deploys both Long Short-Term Memory (LSTM) and Mobile‑BERT machine learning models for real-time web attack detection and classification via a FastAPI server.

---

## Contributors

- [@mishraprayash](https://github.com/mishraprayash)
- [@ashimkarki](https://github.com/Ashimkarrki)
- [@nirajneupane](https://github.com/patali09)
- [@nilumahato](https://github.com/nilumahato)


## 📂 Project Structure

```
.
├── app/
│   ├── background_tasks.py    # Background job definitions
│   ├── config.py              # Application and database settings
│   ├── db.py                  # Database connectivity
│   ├── main.py                # FastAPI application and routes
│   ├── model.py               # Model loading and inference logic
│   ├── predictor.py           # Prediction orchestration
│   ├── preprocessing.py       # Request data cleaning and tokenization
│   ├── schema.py              # Pydantic request/response schemas
│   ├── ai_model/              # Trained models and resources
│   │   ├── bert_model.pth
│   │   ├── custom_keywords.txt
│   │   ├── lstm_model.pt
│   │   └── lstm_vocab.pth
│   └── test/                  # Test scripts
│       ├── local_test_model.py
│       ├── requestgenerator.py
│       └── test_api.py
├── environment.yml            # Conda environment definition
├── requirements.txt           # Python dependencies
├── setup_and_run.sh           # Automated setup & launch script
├── .gitignore
└── README.md
```

---

## 🚀 Prerequisites

* **Python**: 3.11 or 3.12
* **Conda** (optional but recommended) or `venv`
* **MySQL** (or another database) configured and reachable
* **Git**

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mishraprayash/Implementation-of-Web-Attack-Detection-and-Classification-System-Using-LSTM.git
cd Implementation-of-Web-Attack-Detection-and-Classification-System-Using-LSTM
```

### 2. Create & Activate Virtual Environment

Choose one of the options below:

* **Conda (recommended):**

  ```bash
  conda create -n webattack_env python=3.11 -y && \
  conda activate webattack_env
  ```

* **`venv`:**

  * macOS/Linux:

    ```bash
    python3 -m venv env && source env/bin/activate
    ```
  * Windows (PowerShell):

    ```bash
    python -m venv env && .\env\Scripts\Activate.ps1
    ```

### 3. Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🛠️ Automated Setup Script

You can automate environment creation, dependency installation, and server launch:

```bash
chmod +x setup_and_run.sh
./setup_and_run.sh
```

> Ensure your database server is running and `DATABASE_URL` in `app/config.py` is correctly set.

---

## 🚀 Running the FastAPI Server

1. **Navigate to the app directory**

   ```bash
   cd app
   ```
2. **Start Uvicorn**

   ```bash
   uvicorn main:app --reload
   ```
3. **Open in Browser**
   Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

> The `--reload` flag enables hot-reload on code changes.

---

## 📡 API Endpoints

### Health Check: `GET /`

* **Description**: Server health status
* **Response**:

  ```json
  {
    "status": "OK",
    "timestamp": "2023-10-01T12:00:00Z"
  }
  ```

### LSTM Prediction: `POST /predict_lstm`

* **Description**: Returns prediction from the LSTM model
* **Request Body**:

  ```json
  {
    "method": "POST",
    "source_ip": "56.34.67.21",
    "host": "example.com",
    "uri": "/login",
    "auth": "Bearer token123",
    "agent": "Mozilla/5.0",
    "cookie": "session=abc123",
    "referer": "https://example.com/home",
    "body": "{ \"username\":\"test\", \"password\":\"test; select * from users; -- OR '1'='1\"}"
  }
  ```
* **Response**:

  ```json
  {
    "prediction": "SQLI",
    "inference_time_ms": 15.234,
    "prediction_probability": 0.9011,
    "malicious": true,
    "model": "LSTM"
  }
  ```

### BERT Prediction: `POST /predict_bert`

* **Description**: Returns prediction from the BERT model
* **Request & Response**: Same schema as `/predict_lstm`, with `mode: "Mobile-BERT"`.

---

## 💡 Example Usage (cURL)

```bash
curl -X POST http://127.0.0.1:8000/predict_lstm \
  -H "Content-Type: application/json" \
  -d '{
      "method": "POST",
      "source_ip": "45.34.189.235",
      "host": "example.com",
      "uri": "/test",
      "auth": "Bearer <token>",
      "agent": "Mozilla/5.0",
      "cookie": "username=John; path=/",
      "referer": "https://example.com",
      "body": "{ \"username\":\"hacker\", \"password\":\"hacked;...\" }"
    }'
```

* **Response**:

  ```json
  {
    "prediction": "SQLI",
    "inference_time_ms": 15.234,
    "prediction_probability": 0.9011,
    "malicious": true,
    "model": "BERT"
  }
  ```

---


## 🙏 Acknowledgements

* **FastAPI**: High-performance Python API framework
* **Uvicorn**: ASGI server for asynchronous apps

---

