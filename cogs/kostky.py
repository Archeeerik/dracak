import discord
from discord.ext  import commands
import os
import datetime
import random
import json

client = commands.Bot(command_prefix = '+')
client.remove_command("help")



class kostky(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("——————————————————\nCommand kostky ✔️")






    @commands.command()
    async def kostky(self,ctx):
        responses = ["1",
                     "2",
                     "3",
                     "4",
                     "5",
                     "6",]
        await ctx.send(f"Hodil si číslo `{random.choice(responses)}` a `{random.choice(responses)}`")



        
def setup(client):
    client.add_cog(kostky(client)) 