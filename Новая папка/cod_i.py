
import pandas as pd
from telethon.sync import TelegramClient


api_id = 25691879
api_hash = '491767d963de9f8623100f36af11c03c'
phone = 'ваш номер телефона, привязанный к профилю'
 
client = TelegramClient(phone, api_id, api_hash)

client.start()
print( client.get_me())