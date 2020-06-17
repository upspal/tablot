import discord
import os
from dotenv import load_dotenv
from terminaltables import AsciiTable
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

# table data
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
gClient = gspread.authorize(creds)

@client.event
async def on_ready():
    print('i\'m ready to get back to work')

@client.event
async def on_message(message):

    if message.content.startswith('$ts show "'):
        if message.content[-1] != '"':
            await message.channel.send('bhai naam toh dhang se likh le')
        else:
            try:
                a = message.content.split('"')
                sheet = gClient.open(a[1]).sheet1
                data = sheet.get_all_records()

                tableData = [[key for key in data[0].keys()]]
                for i in data:
                    val = [value for value in i.values()]
                    tableData.append(val)

                table = AsciiTable(tableData)
                await message.channel.send(f'```{table.table}```')
            except:
                await message.channel.send('pls junos dis is incorrect file name')

    if message.content.startswith('$ts about'):
        embed = discord.Embed(title='Thanks for adding me to your server! :heart:', description='To get started, simply share your google sheet with me at `mihir-462@tablot-280404.iam.gserviceaccount.com`, and type `$ts help` for a list of commands', colour=1499502).add_field(
            name='Tablot',
            value='Tablot helps you conveniently display your google sheets data on a discord server',
            inline=False).add_field(
            name='Contribute',
            value='We gladly accept contributions. To get started, ' +
            'check out [Tablot\'s GitHub repo](https://github.com/techsyndicate/tablot)',
            inline=False
        ).set_footer(text='Made by Tech Syndicate', icon_url='https://techsyndicate.co/img/logo.png')
        await message.channel.send(embed=embed)

client.run("NzIyMzQzMTc1MzEzOTQ4Njgy.XuhspQ.sfbLozxqI-3qEbNIJzg4-DQiJrA")

# web scraping - future?
# email: mihir-462@tablot-280404.iam.gserviceaccount.com

'''
Commands: 
1. $ts about - bot introduces itself ($hello --> $about)
2. $ts ping - check the bot's latency (j)
3. $ts github - display github repo (j)
4. $ts stats - as the name suggests 
4. ts show "file name"

6. $ts sheet name rachit
serial number: 1
name: Rachit
class: XI - C
stream: science
'''


