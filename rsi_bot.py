from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Load from .env
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@app.route('/', methods=['POST'])
def alert():
    data = request.get_json()
    message = f"📉 RSI Alert Received:\n\n{data}"
    
    # Send to Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    
    response = requests.post(telegram_url, json=payload)
    return {'status': 'ok'}, response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
