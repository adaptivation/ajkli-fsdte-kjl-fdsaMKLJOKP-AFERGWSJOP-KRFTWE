'''
The below code is redistributed under the MIT license
Instructions will be posted sooner or later
'''

from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import datetime
import discord





Client = discord.Client()
client = commands.Bot(command_prefix = "~")


#Checking local machine time async 
async def add_match(arg1,arg2):
    try:
        file = open("matches.txt", "a")
        file.write("\n" + str(arg1)+ " " +str(arg2))
        file.close()
    except:
        embed = discord.Embed(title="ERROR", description="Please contact the developer")
        await client.send_message(await client.send_message(message.channel, embed=embed))
    file.close()
@client.event
async def on_ready():

    print("Bot is ready")
    await client.change_presence(game=discord.Game(name='play.olympusnetwork.eu'))

@client.event
async def on_message(message):
    canceled = False
    #NEW UHC COMMAND
    
    if message.content.upper().startswith('~ADDHOST'):
        if "435514545348411402" in [role.id for role in message.author.roles]:       #Change this with your role's ID
            embed = discord.Embed(title="Olympus Hosts", description="Please insert a time for the host to take place (Type cancel to cancel)", color=0x660033)
            await client.send_message(message.channel, embed=embed)
            response = await client.wait_for_message(author=message.author, timeout=60)
            time_input = response.clean_content.upper()
    
            
                
            #DAY INSERT CODE
            if response.clean_content.upper() != "CANCEL": 
            
                response = response.clean_content
                embed = discord.Embed(title="Olympus Hosts", description="Ok, insert a day now (Type cancel to cancel)", color=0x660033)
                await client.send_message(message.channel, embed=embed)
                response = await client.wait_for_message(author=message.author, timeout=60)
                day_input = response.clean_content.upper()
                
            else:
                if canceled:
                    pass
                else:
                    embed = discord.Embed(title="Olympus Hosts", description="Cancelled!", color=0xCC0000)
                    await client.send_message(message.channel, embed=embed)
                    canceled = True
                
                
            #SCENARIOS INSERT CODE
            if response.clean_content.upper() != "CANCEL": 
            
                response = response.clean_content
                embed = discord.Embed(title="Olympus Hosts", description="Ok, insert the scenarios now (Type cancel to cancel)", color=0x660033)
                await client.send_message(message.channel, embed=embed)
                response = await client.wait_for_message(author=message.author, timeout=60)
                scenarios_input = response.clean_content.upper()
                
            else: 
                if canceled:
                    pass
                else:
                    embed = discord.Embed(title="Olympus Hosts", description="Cancelled!", color=0xCC0000)
                    await client.send_message(message.channel, embed=embed)
                    canceled = True
    
    
            #MODE INSERT CODE
            if response.clean_content.upper() != "CANCEL": 
            
                response = response.clean_content
                embed = discord.Embed(title="Olympus Hosts", description="Ok, insert the mode now (Type cancel to cancel)", color=0x660033)
                await client.send_message(message.channel, embed=embed)
                response = await client.wait_for_message(author=message.author, timeout=60)
                mode_input = response.clean_content.upper()
                
            else: 
                if canceled:
                    pass
                else:
                    embed = discord.Embed(title="Olympus Hosts", description="Cancelled!", color=0xCC0000)
                    await client.send_message(message.channel, embed=embed)
                    canceled = True
                
                
            #HOST INSERT CODE
            if response.clean_content.upper() != "CANCEL": 
            
                response = response.clean_content
                embed = discord.Embed(title="Olympus Hosts", description="Ok, insert the host now (Type cancel to cancel)", color=0x660033)
                await client.send_message(message.channel, embed=embed)
                response = await client.wait_for_message(author=message.author, timeout=60)
                host_input = response.clean_content.upper()
                
            else: 
                if canceled:
                    pass
                else:
                    embed = discord.Embed(title="Olympus Hosts", description="Cancelled!", color=0xCC0000)
                    await client.send_message(message.channel, embed=embed)
                    canceled = True
                    
                    
        else:
            embed = discord.Embed(title="Olympus Hosts", description="You do not have permission!", color=0xCC0000)
            await client.send_message(message.channel, embed=embed)
            
            
        if not canceled:
            embed = discord.Embed(title="NEW HOST", description = "There is a new scheduled host", color=0x800080)
            embed.set_thumbnail(url="https://i.imgur.com/DD5hyRO.jpg")
            embed.add_field(name="Time/Day", value=" TIME " + time_input +" |~| DAY "+ day_input)
            embed.add_field(name="Scenarios", value=scenarios_input)
            embed.add_field(name="Mode", value=mode_input)
            embed.add_field(name="Host", value=host_input)
            embed.set_footer(text="IP: play.olympusnetwork.eu")
            await client.send_message(client.get_channel("435514441052717057"), embed=embed)       #Change this with your channel's ID     
            await client.send_message(client.get_channel("435514441052717057"), "@everyone")       #Change this with your channel's ID 
            
            await add_match(time_input,day_input)
        
 



client.run("")
