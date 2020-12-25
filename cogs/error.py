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




class Chyba(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("——————————————————\nCommand Errors ✔️")



    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(":x:│Špatně si napsal příkaz.")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(":no_entry:│Nemáš oprávnění na použití tohoto příkazu.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(":x:│Doplň věci, které v příkaze chybí.")
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f":no_entry:│Tento příkaz lze zopakovat za **{error.retry_after:,.0f} sekund**.")
        






def setup(client):
    client.add_cog(Chyba(client))  