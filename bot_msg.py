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
    await message.reply("""Olá eu sou o ChamberlinBot.
    Comandos:
    /select
    /from
    """) 

@app.on_message(filters.command('select'))
async def case(client, message):
    print(message.chat.username, message.text)
    await message.reply("""
    A principal função do **SELECT** é consultar/buscar os dados de uma tabela em um banco de dados. O caracter * retorna todas as colunas da tabela pesquisada.
    Exemplo: 
 select * from departamento;

DEPART     DNOME        UF
------ -------------- ---------
 10     ACCOUNTING      BH
 20     RESEARCH        SP
 30     SALES           RS
 40     OPERATIONS      BA
 """ )

@app.on_message(filters.command('from'))
async def case(client, message):
    print(message.chat.username, message.text)
    await message.reply(
        """
        O comando **FROM** é usado para especificar de qual tabela selecionar ou excluir dados.
         Exemplo: 

        select * from departamento;
        DEPART     DNOME        UF
      ------ -------------- ---------
        10     ACCOUNTING      BH
        20     RESEARCH        SP
        30     SALES           RS
        40     OPERATIONS      BA

       Outros exemplos onde exigirão uma declaração From com uma palavra-chave, até mesmo para selecionar dados do sistema.
        Exemplo:

        select to_char(sysdate, 'Dy DD-Mon-YYYY HH24:MI:SS')
        as "Current Time"
        from dual;

        """
        )


@app.on_message()
async def messages(client, message):
    print(message.chat.username, message.text)
    await message.reply('Desculpe, o comando ' + '"' + message.text + '"' + ' não é um comando valido ao ainda não o aprendi.' )

app.run()