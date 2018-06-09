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


@client.event
async def on_message(message):
    canceled = False
    #NEW UHC COMMAND
    
    if message.content.upper().startswith('~NEWGAME'):
        if "435514545348411402" in [role.id for role in message.author.roles]:       #Change this with your role's ID  // Checking for appropriate role
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
            embed = discord.Embed(title="NEW HOST", description = "There is a new scheduled host for " + day_input + " at " + time_input, color=0x800080)
            embed.set_thumbnail(url="https://i.imgur.com/gXGuqNh.png")
            embed.add_field(name="**MATCH DETAILS**", value="\n\n**SCENARIOS** " +scenarios_input + "\n\n**MODE** " +mode_input + "\n\n**HOST** " +host_input + "\n")  #" **TIME** " + time_input +"\n**DAY** "+ day_input + 
            embed.set_footer(text="IP: play.olympusnetwork.eu")
            await client.send_message(client.get_channel("435514441052717057"), embed=embed)       #Change this with your channel's ID     
            await client.send_message(client.get_channel("435514441052717057"), "@everyone")       #Change this with your channel's ID
    
    if message.content.upper().startswith('~WLOFF'):
        if "435514545348411402" in [role.id for role in message.author.roles]:       #Change this with your role's ID  // Checking for appropriate role
            embed = discord.Embed(title="WHITELIST OFF", description="The planned game will be starting soon", color=0x800080)
            embed.set_thumbnail(url="https://i.imgur.com/gXGuqNh.png")
            embed.set_footer(text="IP: play.olympusnetwork.eu")
            await client.send_message(client.get_channel("435514441052717057"), embed=embed)       #Change this with your channel's ID     
            await client.send_message(client.get_channel("435514441052717057"), "@everyone")       #Change this with your channel's ID


client.run("NDM3MzA1MTQxMjM0ODkyODEw.Df2hqA.OR9oHSsUMDxqOd8ib6Vez8_xxlc")
