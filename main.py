from pyrogram import Client, filters
from requests import get
from config import *
import asyncio

Bot = Client(
	"trlink",
	api_id=api_id,
	api_hash=api_hash,
	bot_token=token
)



@Bot.on_message(filters.all & filters.private)
async def trlink(client: Bot, message):
	if message.from_user.id in sudo:
		web = message.text
		link = get(f"https://tr.link/api/?api={key}&url={web}&alias=&format=text&ct=1").text
		await asyncio.sleep(0.7)
		await message.reply_text(f"**Link;\n\n{link}**")


print("Bot çalıştı!")
Bot.run()
