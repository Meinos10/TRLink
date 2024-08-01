from pyrogram import *
from pyrogram.types import *
from config import *
import os, request as req

Bot = Client(
	"trlink",
	api_id=api_id,
	api_hash=api_hash,
	bot_token=token
)

def delete_cmd_history():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")


def url_btn(url):
	BUTTON = [[InlineKeyboardButton("TrLink", url=url)]]
	return InlineKeyboardMarkup(BUTTON)

@Bot.on_message(filters.all & filters.private)
async def trlink(client: Bot, message: Message):
	if message.from_user.id in sudo:
		if not message.text:
			return await client.send__message(message.chat.id, "**Only url!**")
			
		try:
			web = str(message.text)
		except Exception as e:
			return await client.send_message(message.chat.id, "**Only `letters`!**")
			
		try:
			result_url = req.get(f"https://tr.link/api/?api={key}&url={web}&alias=&format=text&ct=1").text
		except Exception as e:
			return await client.send_message(message.chat.id, "Error: `{}`".format(str(e)))
			
		return await message.reply_text(f"**URL: `{result_url}`**", url_btn(result_url))


delete_cmd_history()
Bot.start()
print("Bot started!")
idle()
