import time
import requests

BOT_TOKEN = "6706163089:AAGUM3ZrfkM6mlpaG0oR8wa4FMT0NbN2p_s"
CHAT_ID = "1016376897"
MESSAGE = "hi"

send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

while True:
    requests.post(send_url, data={"chat_id": CHAT_ID, "text": MESSAGE})
    print("Message sent!")
    time.sleep(20)  # wait 10 seconds