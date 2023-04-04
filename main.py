import asyncio
import discord
import json
import os
import colorama
import random
import datetime
import requests
import ctypes

from colorama import Fore
from pystyle import Colors, Colorate
from discord.ext import commands

with open("config.json") as f:
    config = json.load(f)
token = config.get("Token")
prefix = config.get("Prefix")
starttime = datetime.datetime.utcnow()

client = commands.Bot(self_bot=True, command_prefix=prefix, case_insensitive=True,)
client.remove_command("help")



async def kd_message():
    await client.wait_until_ready()
    while True:
        channel = client.get_channel(1081971333602234448) # replace with your desired channel id
        await channel.send('kd')

        try:
            message = await client.wait_for('message', check=lambda m: m.author.id == 646937666251915264 and m.channel == channel, timeout=60.0)
            choices = [1, 2, 3]
            choice = random.choice(choices)
            await asyncio.sleep(random.randint(2, 5))  # wait 2-5 seconds before reacting
            if choice == 1:
                await message.add_reaction("1️⃣")
            elif choice == 2:
                await message.add_reaction("2️⃣")
            elif choice == 3:
                await message.add_reaction("3️⃣")
        except asyncio.TimeoutError:
            pass  # ignore timeout errors and continue the loop 

        await asyncio.sleep(random.randint(1800, 2400))  # wait for 30-40 minutes before sending another message

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    client.loop.create_task(kd_message()) 
 

 
client.run(token)


