import mcstatus
from mcstatus import MinecraftServer
import time
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

#Comment Test
TOKEN = "Nzg1MDA4MjUyODIzNjY2Njg5.X8xl6A.GQZm9_15HjcXqHJ7rTN1WWnQ4R8"
client = commands.Bot(command_prefix = '.')
channel_id = 777514695799210034
server_name = "Holiday"
server_ip = "Holiday.ploudos.me"

#If there are no players online, the server is read as offline
def getStatus(server):
    server = MinecraftServer.lookup(server)
    status = server.status()

    if status.players.online <= 0:
        return f"|{server_name}|Offline|N/A|"
    
    else:
        return f"|{server_name}|Online|*{status.players.online}*"

@client.event
async def on_ready():
    print("Bot is ready")

    #Checks every 5 seconds for the status, updates if status is changed
    check = None
    while True:
        new_checker = getStatus(server_ip)

        if new_checker != check:
            channel = client.get_channel(channel_id)
            await channel.purge(limit = 1, check = lambda m: m.author == client.user)
            await channel.send(getStatus(server_ip))

        check = new_checker

        time.sleep(5)   


 

client.run(TOKEN)