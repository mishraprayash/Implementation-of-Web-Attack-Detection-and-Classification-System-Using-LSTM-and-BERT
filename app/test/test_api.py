import requests
import json
import time

# Define the API endpoint (update this if running on a different host)
API_URL = "http://127.0.0.1:8000/predict"

# Sample request data (modify as needed)
test_data = {
    "host": "example.com",
    "uri": "/login",
    "auth": "Bearer token123",
    "agent": "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "cookie": "session=abc123; path=/",
    "referer": "https://example.com/home",
    "body": "SELECT * FROM users WHERE username='admin' --"
}

# Convert to JSON format
json_data = json.dumps(test_data)

# Measure request time
start_time = time.time()

try:
    # Send a POST request to the API
    response = requests.post(API_URL, data=json_data, headers={"Content-Type": "application/json"})

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
