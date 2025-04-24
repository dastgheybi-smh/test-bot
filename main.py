import time
import requests

def get_updates(offset=None):
    url = f"https://tapi.bale.ai/bot1706768140:wT6bwSo7YUrosVf3IrMSjfmIVtnhTcsuRKU5Qrpy/getUpdates"
    if offset:
        url += f"?offset={offset}"
    response = requests.get(url)
    return response.json()

def send_message(chat_id, text):
    url = f"https://tapi.bale.ai/bot1706768140:wT6bwSo7YUrosVf3IrMSjfmIVtnhTcsuRKU5Qrpy/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def handle_message(message):
    chat_id = message['chat']['id']
    text = message.get('text', '')
    send_message(chat_id, text)

last_update_id = None

while True:
    updates = get_updates(last_update_id)
    for update in updates.get("result", []):
        if "message" in update:
            handle_message(update["message"])
            last_update_id = update["update_id"] + 1
    time.sleep(1)
