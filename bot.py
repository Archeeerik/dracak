import discord
import csv
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

TOKEN = "YOURTOKEN"

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Krasne Vanoce | Archer#0579"))
    print("Bot is ready")



@client.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: **Pong!**  `{round(client.latency * 1000)}ms`')
    
    
    
@client.command()
async def embed(ctx, title, text):
    embed = discord.Embed(
        title = f'{title}',
        description = f'{text}',
        color = discord.Color.red()
    )
    await ctx.send(embed=embed)
    


#družinky---------------------------------------------------------------------------------------------------------------
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id ==791819393822359553:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == "snek":
                role = discord.utils.get(guild.roles, name="Lovci šneků")
        elif payload.emoji.name == "dragoni":
                role = discord.utils.get(guild.roles, name="Dragoni")
        
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("Role přiřazena ")
            else:
                print("Uživatel nenalezen")
        else:
            print("Role nenalezena")


    message_id = payload.message_id
    if message_id ==791825932049842206:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == "goblin":
                role = discord.utils.get(guild.roles, name="Goblin")
        elif payload.emoji.name == "maxe":
                role = discord.utils.get(guild.roles, name="Trpaslík")
        elif payload.emoji.name == "mbow":
                role = discord.utils.get(guild.roles, name="Elf")
        elif payload.emoji.name == "msword":
                role = discord.utils.get(guild.roles, name="Seveřan")
        
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("Role přiřazena ")
            else:
                print("Uživatel nenalezen")
        else:
            print("Role nenalezena")


    

client.load_extension("cogs.error")
client.load_extension("cogs.kostka")
client.load_extension("cogs.kostky")
client.load_extension("cogs.pomoc")
client.load_extension("cogs.smaz")
client.run(TOKEN)
