from pyrogram import Client, filters

app = Client(
    "my_bot",
    api_id=123456,
    api_hash="your_api_hash",
    bot_token="8139101323:AAEcT5Tny_PEerVqFuLOtjqdBekpivq4G-k"
)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Бот работает! 🔥")

app.run()
