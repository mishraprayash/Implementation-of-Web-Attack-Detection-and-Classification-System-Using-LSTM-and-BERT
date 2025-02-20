
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

It is recommended to create a virtual environment to manage dependencies. Note: Use the stable version of python supporting the below used dependecies. You can use python@3.11 while creating your virtual environent.


### Using Conda environment

For the most lazy people, you can create virtual enviroment, install dependencies and run the server all together using a single script. But before that, make sure you have configured your database server. Here, I am using MySQL database. 

If you are testing locally, you need to run the database server. If your database is hosted on a remote server, you can update the DATABASE_URL from config.py.

[Refer here](#bash-automation) for bash script.

#### Manual Installtion

You must have already installed conda to use this.

```bash
# create an environment
# pip comes installed while creating this environment

conda create -n test_env python=3.11 
conda activate test_env

# you can use pip as well conda(with specific channels if needed)
pip install -r requirements.txt 

```

#### Alternative installation using environment.yml 

The environemt.yml file contains the env name, conda channels(we can change it as per the requirements), and the dependencies. If the dependencies arenot available through the conda channel, we can use pip for installing those dependencies.

```bash
conda env create -f environment.yml 

```

### System-Specific Installtion

Use the stable version of python such as python@3.11 or python@3.12
#### On macOS/Linux:

```bash
python3.12 -m venv test_env
source test_env/bin/activate
```

#### On Windows:

```bash
python -m venv test_env
test_env\Scripts\activate
```

#### Install Dependencies

With the virtual environment activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

# Bash Automation

```bash
cd Implementation-of-Web-Attack-Detection-and-Classification-System-Using-LSTM
chmod +x setup_and_run.sh 
./setup_and_run

```

## Running the FastAPI Server

Uvicorn is an Asynchronous Server Gateway Interface (ASGI) used to handle web application enabling asynchronous programming and better performance over traditional WSGI. You can read about it more [here](https://www.uvicorn.org/).

Make sure your database is properly configured before running this.

Start the FastAPI server using Uvicorn:

```bash
cd app/
uvicorn main:app --reload
```

- The server will run at [http://127.0.0.1:8000](http://127.0.0.1:8000).
- The `--reload` flag enables automatic reloading during development when code changes occur.

## API Endpoints



### `/health/` (GET)
- **Description:** Checks the health status of the server.
- **Response Example:**

  ```json
  {
    "status": "OK"
  }
  ```

### `/predict/` (POST)
- **Description:** Accepts input data in JSON format and returns a prediction from the machine learning model.
- **Request Body Example:**

  ```json
  {
    "method":"POST",
    "source_ip":"56.34.67.21",
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



## Example Usage

You can test the API using `curl` or any API testing tool like Postman. For example, to test the prediction endpoint with `curl`:

```bash
curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "method":"POST",
  "source_ip":"45.34.189.235",
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


