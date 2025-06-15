import os
from pyrogram import Client

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

app = Client("my_bot", api_id=api_id, api_hash=api_hash)

@app.on_message()
def handle(client, message):
    print(f"Новое сообщение: {message.text}")

app.run()
