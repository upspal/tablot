import discord
import os
from dotenv import load_dotenv
from terminaltables import AsciiTable
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

# table data
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
gClient = gspread.authorize(creds)
sheetName = input('Enter the name of your sheet: ')
sheet = gClient.open(sheetName).sheet1
data = sheet.get_all_records()

tableData = [[key for key in data[0].keys()]]
for i in data:
    val = [value for value in i.values()]
    tableData.append(val)

table = AsciiTable(tableData)

@client.event
async def on_ready():
    print('i\'m ready to get back to work')

@client.event
async def on_message(message):

    if message.content.startswith('$hello'):
        await message.channel.send(f'```{table.table}```')

client.run(TOKEN)
