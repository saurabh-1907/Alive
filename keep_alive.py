import requests
import schedule
import time
from flask import Flask

app = Flask(__name__)

TARGET_URL = "https://thread-clone-j581.onrender.com/"
SELF_URL = "https://alive-1-dqhi.onrender.com"  # Replace with your Render app URL

def send_request():
    try:
        response = requests.get(TARGET_URL)
        print(f"Request to {TARGET_URL} sent: {response.status_code}")
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
schedule.every(10).minutes.do(keep_alive)  # Self-ping to stay alive

# Flask route to keep Render happy
@app.route('/')
def home():
    return "I'm alive!"

@app.route('/ping')
def ping():
    return "Pong"

# Run Flask and schedule in parallel
if __name__ == "__main__":
    from threading import Thread

    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    Thread(target=run_schedule).start()
    app.run(host="0.0.0.0", port=10000)  # Render requires a running web service
