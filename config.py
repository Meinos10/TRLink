from os import getenv


api_id = int(getenv("API_ID", 18170822))
api_hash = getenv("API_HASH", "ef37e3822315ab88a12d65589bd83c0c")
token = getenv("BOT_TOKEN", "5721410098:AAEKRUBFNOn6MzxfjeOMH4rW4ZGl183Mmm0")
sudo = list(map(int, getenv("SUDO", [1838880460, 1339844465, 1311433270]).split()))
key = getenv("API_KEY", "4d2c53f41f7b5dd725a61a86f5651ccfae8c65f8")
