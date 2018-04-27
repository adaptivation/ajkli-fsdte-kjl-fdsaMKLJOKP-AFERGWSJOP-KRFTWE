from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import datetime
import discord

Client = discord.Client()
client = commands.Bot(command_prefix = "~")


@client.event
async def on_ready():

    print("Bot is ready")
    await client.change_presence(game=discord.Game(name='play.olympusnetwork.eu'))


async def check_time():
            

    broke = False
            

    while True:
        now = time.strftime("%H:%M")
        now2 = time.strftime("%d/%m")
        print("Now:", now,now2 )
        try:
            file = open("matches.txt", "r")
        except FileNotFoundError:
            embed = discord.Embed(title="ERROR", description="Please contact the developer \\ Error Code: 4")
            embed.set_footer(text="Check procedure has been terminated!")
            await client.send_message(message.channel, embed=embed)
            break
        file.seek(0)
        time.sleep(5)
        for i in file:
            if i[0:5] == now:
                print("1")
                if i[6:len(i)] == now2:
                    print("2")
                    embed = discord.Embed(title="WHITELIST IS OFF", description="Whitelist is now disabled, and game will be starting soon", color=0x800080)
                    embed.set_thumbnail(url="https://i.imgur.com/DD5hyRO.jpg")
                    embed.set_footer(text="IP: play.olympusnetwork.eu")
                    await client.send_message(client.get_channel("435514441052717057"), embed=embed)       #Change this with your channel's ID 
                    await client.send_message(client.get_channel("435514441052717057"), "@everyone")       #Change this with your channel's ID
                    break
        try:
            file.close()
        except:
            print("Could not close")
                    
                    
                    
@client.event
async def on_message(message):
    #COMMAND
    
    if message.content.upper().startswith('~BOTSTART'):
        if "435514545348411402" in [role.id for role in message.author.roles]:       #Change this with your role's ID
            print("Starting check_time()")
            
            await check_time()
            
client.run("")
