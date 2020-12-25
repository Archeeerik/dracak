import discord
import os
import random
from discord.ext  import commands
from pathlib import Path
import platform
import logging
import datetime
import asyncio
from discord.ext.commands import Bot
import logging
from discord.utils import get
import json
from discord import DMChannel
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

client = commands.Bot(command_prefix = '+', intents = intents)
client.remove_command("help")




class smaz(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("——————————————————\nCommand $vymaz ✔️")




     
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def smaz(self, ctx, amount=0):
        if amount <= 0:
            await ctx.send(":x:│Musíš zadat počet zpráv, které chceč vymazat.")
        if amount > 0:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f":white_check_mark:| Bylo úspěšně odstraněno {amount} zpráv.", delete_after = 2)





            
def setup(client):
    client.add_cog(smaz(client)) 