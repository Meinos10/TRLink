from pyrogram import Client, filters
from requests import get
from config import *


Bot = Client(
	"trlink",
	api_id=api_id,
	api_hash=api_hash,
	bot_token=token
)



@Bot.on_message(filters.text & filters.private)
async def trlink(client: Bot, message):
	if message.from_user.id in sudo:
		web = message.text
		link = get("https://tr.link/api/?api={}&url={}&alias=&format=text&ct=1".format(key, web)).text
		await client.send_message(message.chat.id, f"**Link;\n\n`{link}`**")


print("Bot çalıştı!")
Bot.run()