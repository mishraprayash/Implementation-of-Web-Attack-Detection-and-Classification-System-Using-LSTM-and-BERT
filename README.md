
# Implemention for Web Attack Detection and Classification using Long Short Term Memory (LSTM)-based Model using FastAPI


##  FastAPI Model Deployment 

This project sets up a FastAPI server to deploy a machine learning model as an API for real-time predictions. The API processes incoming requests and returns model predictions based on input data. This guide provides instructions for setting up the development environment, running the server, and understanding the project structure.

## Project Structure

```
app/
├── background_tasks.py    
├── config.py               
├── db.py                  
├── lstm_model/            
│   ├── model.pt           
│   └── vocab.pth          
├── model.py               
├── main.py                
├── predictor.py          
├── preprocessor.py        
├── schema.py                         
├── test/                 
│   └── ...                
requirements.txt 
.gitignore  
```

## Installation and Setup

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/mishraprayash/Implementation-of-Web-Attack-Detection-and-Classification-System-Using-LSTM
cd Implementation-of-Web-Attack-Detection-and-Classification-System-Using-LSTM
```

### 2. Setup Virtual Environment

It is recommended to create a virtual environment to manage dependencies.

#### On macOS/Linux:

```bash
python3 -m venv test_env
source test_env/bin/activate
```

#### On Windows:

```bash
python -m venv test_env
test_env\Scripts\activate
```

### 3. Install Dependencies

With the virtual environment activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the FastAPI Server

Uvicorn is an Asynchronous Server Gateway Interface (ASGI) used to handle web application enabling asynchronous programming and better performance over traditional WSGI. You can read about it more [here](https://www.uvicorn.org/).

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

- The server will run at [http://127.0.0.1:8000](http://127.0.0.1:8000).
- The `--reload` flag enables automatic reloading during development when code changes occur.

## API Endpoints

### `/predict/` (POST)
- **Description:** Accepts input data in JSON format and returns a prediction from the machine learning model.
- **Request Body Example:**

  ```json
  {
    "method":"POST",
    "source_ip":"34.98.121.202",
    "host": "example.com",
    "uri": "/login",
    "auth": "Bearer token123",
    "agent": "Mozilla/5.0",
    "cookie": "session=abc123",
    "referer": "https://example.com/home",
    "body": "{\"username\":\"test\", password:\"test; select * from users; -- OR '1'='1\"}"
  }
  ```

- **Response Example:**

  ```json
  {
    "prediction": "SQLI",
    "prediction_probability":0.901121,
    "inference_time_ms":20.239
  }
  ```

### `/health/` (GET)
- **Description:** Checks the health status of the server.
- **Response Example:**

  ```json
  {
    "status": "OK"
  }
  ```

## Example Usage

You can test the API using `curl` or any API testing tool like Postman. For example, to test the prediction endpoint with `curl`:

```bash
curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "method":"POST",
  "source_ip":"34.98.121.202",
  "host": "example.com",
  "uri": "/test",
  "auth": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
  "agent": "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
  "cookie": "username=John Doe; expires=Thu, 18 Dec 2013 12:00:00 UTC; path=/",
  "referer": "https://example.com/refer",
  "body": "{\"username\":\"hacker\", \"password\":\"hacked; select * from user where user='admin' OR '1'='1' --\"}"
}'
```


## Acknowledgements

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Uvicorn**: A lightning-fast ASGI server for running FastAPI apps.


