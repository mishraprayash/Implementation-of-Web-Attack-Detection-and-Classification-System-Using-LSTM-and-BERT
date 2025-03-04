import requests
import json
import time

# Define the API endpoint (update this if running on a different host)
API_URL_LSTM = "http://0.0.0.0:8000/predict_lstm" 
API_URL_BERT = "http://0.0.0.0:8000/predict_bert"

# Sample request data (modify as needed)
test_data = {
    "method":"PUT",
    "source_ip":"192.168.1.56",
    "host": "example.com",
    "uri": "/login",
    "auth": "",
    "agent": "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "cookie": "",
    "referer": "https://example.com/home",
    "body": ''
}

# Convert to JSON format
json_data = json.dumps(test_data)

# Measure request time
start_time = time.time()

try:
    # Send a POST request to the API
    response = requests.post(API_URL_LSTM, data=json_data, headers={"Content-Type": "application/json"})

    # Measure response time
    elapsed_time = time.time() - start_time

    # Print the response
    if response.status_code == 200:
        print("✅ API Response:", response.json())
        print(f"⏱️ Response Time: {elapsed_time:.5f} sec")
    else:
        print("❌ API Error:", response.status_code, response.text)

except requests.exceptions.RequestException as e:
    print("❌ Request Failed:", e)
