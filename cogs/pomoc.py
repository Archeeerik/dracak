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

colour = [0xaff00]




class pomoc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("——————————————————\nCommand +pomoc ✔️")





    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def pomoc(self, ctx):
        ctx = ctx.message.channel

        embed = discord.Embed(
            title = "Pomoc",
            color=random.choice(colour)
        )
        embed.add_field(name="Prefix", value="Prefix bota je +")
        embed.add_field(name="+pomoc", value="Pošle seznam příkazů",inline=False)
        embed.add_field(name="+kostka", value="Hodíte jednou kostkou",inline=False)
        embed.add_field(name="+kostky", value="Hodíte dvěmi kostkami",inline=False)
        embed.set_footer(text="Developed by Archer", icon_url="https://media.discordapp.net/attachments/790652943756951575/791800183250878464/IMG_20201224_233841.jpg")

        await ctx.send(embed=embed)






def setup(client):
    client.add_cog(pomoc(client))