import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio, random, os, time, psycopg2


try:
    from config import TOKEN
except ModuleNotFoundError:
    TOKEN = os.environ["TOKEN"]


client = discord.Client()
prefix = "d."
cleint = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(activity = discord.Game(name="Say d.help"))
    await onlinestuff()

async def onlinestuff():
    global server, channnel, wiiu, switch, na, eu, naflag, euflag, wiiuflag, switchflag
    server = discord.get_guild(428632636492087296)
    channel = discord.utils.get(server.channels, name = "gateway-2")
    wiiu = discord.utils.get(server.roles, name = "Wii U Owner")
    switch = discord.utils.get(server.roles, name = "Switch Owner")
    na = discord.utils.get(server.roles, name = "NA/AU/NZ Player")
    eu = discord.utils.get(server.roles, name ="EU Player")
    naflag = "{}{}".format(u"\U0001F1FA",u"\U0001F1F8")
    euflag = "{}{}".format(u"\U0001F1EA",u"\U0001F1FA")
    wiiuflag = u"\U0001F535"
    switchflag = u"\U0001F534"
    roles = {naflag: na, euflag: eu, wiiuflag: wiiu, switchflag: switch}


@client.event
async def on_raw_reaction_add(payload):
    global person
    await person.send(payload)"""
    global server, channel, wiiu, switch, na, eu, naflag, euflag, wiiuflag, switchflag
    if reaction.message.channel == channel:
        try:
            role = roles[reaction.emoji]
            await user.add_roles(role)
        except KeyError:
            pass
"""
client.run(TOKEN)      
