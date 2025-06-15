from pyrogram import Client
import asyncio

api_id = 12345678  # ← сюда вставь свой api_id
api_hash = "your_api_hash_here"  # ← сюда вставь свой api_hash
bot_token = "8139101323:AAEcT5Tny_PEerVqFuLOtjqdBekpivq4G-k"  # ← это уже твой токен

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message()
async def handler(client, message):
    await message.reply("Бот работает ✅")

async def main():
    await app.start()
    print("Бот запущен...")
    await asyncio.Event().wait()  # Ожидаем бесконечно, чтобы не завершалось

if __name__ == "__main__":
    asyncio.run(main())
