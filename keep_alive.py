import requests
import schedule
import time

URL = "https://thread-clone-j581.onrender.com/"
SELF_URL = "https://your-own-app.onrender.com/ping"  # Replace with your own app URL

def send_request():
    try:
        response = requests.get(URL)
        print(f"Request to {URL} sent: {response.status_code}")
    except Exception as e:
        print(f"Error sending request: {e}")

def keep_alive():
    try:
        response = requests.get(SELF_URL)
        print(f"Self-ping successful: {response.status_code}")
    except Exception as e:
        print(f"Error self-pinging: {e}")

# Schedule tasks
schedule.every(14).minutes.do(send_request)
schedule.every(10).minutes.do(keep_alive)  # Keep the script alive

# Run loop
while True:
    schedule.run_pending()
    time.sleep(1)
