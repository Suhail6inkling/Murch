import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio, random, os, time#, psycopg2


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
    global server, channnel, wiiu, switch, na, eu, naflag, euflag, wiiuflag, switchflag, person, message, roles
    person = client.get_user(131131701148647424)
    server = client.get_guild(428632636492087296)
    print(person,server)
    channel = discord.utils.get(server.channels, name = "gateway-2")
    message = await channel.get_message(449977173059829760)
    print(message)
    wiiu = discord.utils.get(server.roles, name = "Wii U Owner")
    switch = discord.utils.get(server.roles, name = "Switch Owner")
    na = discord.utils.get(server.roles, name = "NA/AU/NZ Player")
    eu = discord.utils.get(server.roles, name ="EU Player")
    naflag = "{}{}".format(u"\U0001F1FA",u"\U0001F1F8")
    euflag = "{}{}".format(u"\U0001F1EA",u"\U0001F1FA")
    wiiuflag = u"\U0001F535"
    switchflag = u"\U0001F534"
    roles = {naflag: na, euflag: eu, wiiuflag: wiiu, switchflag: switch}
    while True:
        await reactioncheck()




async def reactioncheck():
    global message, roles
    a = []
    for x in server.members:
        a.append([x])
    reactions = message.reactions
    for reaction in reactions:
        #try:
            role = roles[reaction.emoji]
            users = await reaction.users().flatten()
            for user in users:
                #try:
                    for p in a:
                        if p[0] == user:
                            p.append(role)
                #except:
                    pass
            
        #except:
            pass
    for c in a:
        for e in roles:
            if len(c) == 1:
                if roles[e] in c[0].roles:
                    await c[0].remove_roles(roles[e])
            else:
                if roles[e] in c:
                    if roles[e] not in c[0].roles:
                        await c[0].add_roles(roles[e])
                else:
                    #print("Bye")
                    if roles[e] in c[0].roles:
                        await c[0].remove_roles(roles[e])
    
client.run(TOKEN)

    
