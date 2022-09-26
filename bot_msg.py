from email import message
from os import getenv
from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv()

app = Client(
    'chamberlin_bot',
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_API_TOKEN')
    )

@app.on_message(filters.command('help'))
async def ajuda(client, message):
    print(message.chat.username, message.text)
    await message.reply('Olá eu sou o ChamberlinBot, essa é uma mensagem de ajuda!') 

@app.on_message()
async def messages(client, message):
    print(message.chat.username, message.text)
    await message.reply('Desculpe, o comando ' + '"'+ message.text+ '"' + ' não é um comando valido ao ainda não o aprendi' )

app.run()