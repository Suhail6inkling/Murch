import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio, random, os, time#, psycopg2
import gsheets
try:
    from config import TOKEN, prefix
except ModuleNotFoundError:
    TOKEN = os.environ["TOKEN"]
    prefix = os.environ["prefix"]


client = discord.Client()
client = commands.Bot(command_prefix=prefix)
startup_extensions=["splatooncommands"]

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(activity = discord.Game(name="Exclusively for 'Splat Hub!'"))
    await onlinestuff()

async def onlinestuff():
    global server, channnel1, person, message1, roles, message2, superseasnail, alerts
    person = client.get_user(131131701148647424)
    server = client.get_guild(428632636492087296)
    
    channel1 = discord.utils.get(server.channels, name = "gateway-2")
    message1 = await channel1.get_message(449977173059829760)
    wiiu = discord.utils.get(server.roles, name = "Wii U Owner")
    switch = discord.utils.get(server.roles, name = "Switch Owner")
    na = discord.utils.get(server.roles, name = "NA/AU/NZ Player")
    eu = discord.utils.get(server.roles, name ="EU Player")
    naflag = "{}{}".format(u"\U0001F1FA",u"\U0001F1F8")
    euflag = "{}{}".format(u"\U0001F1EA",u"\U0001F1FA")
    wiiuflag = u"\U0001F535"
    switchflag = u"\U0001F534"
    roles = {naflag: na, euflag: eu, wiiuflag: wiiu, switchflag: switch}
    
    #channel2 = discord.utils.get(server.channels, name= "server-updates")
    #message2 = await channel2.get_message(451113983345164289)
    #superseasnail = discord.utils.get(server.emojis, name="SuperSeaSnail")
    #alerts = discord.utils.get(server.roles, name = "Alerts")
   
    while True:
        await reactioncheck1()
        #await reactioncheck2()



@client.event
async def on_member_join(member):
    gsheets.open()
    values = [gsheets.lenrows(),str(member.id)]
    for x in range(0, 28):
        values.append("None")
        gsheets.addrow(values)

@client.event
async def on_member_remove(member):
    gsheets.open()
    people = gsheets.read()
    for x in people:
        if x["ID"] == member.id:
            personlist = x
    gsheets.delrow(personlist["Place in Queue"])


async def reactioncheck1():
    global message1, roles
    a = []
    for x in server.members:
        a.append([x])
    reactions = message1.reactions
    for reaction in reactions:
            role = roles[reaction.emoji]
            users = await reaction.users().flatten()
            for user in users:
                    for p in a:
                        if p[0] == user:
                            p.append(role)
                    pass
            pass
    for c in a:
        for e in roles:
                if roles[e] in c:
                    if roles[e] not in c[0].roles:
                        await c[0].add_roles(roles[e])  
                        print(c[0], roles[e], "+")
                else:
                    if roles[e] in c[0].roles:
                        await c[0].remove_roles(roles[e])
                        print(c[0], roles[e], "-")
    
async def reactioncheck2():
    global message2, superseasnail, alerts
    a = []
    for x in server.members:
        a.append([x,False])
    reactions = message2.reactions
    for reaction in [q for q in reactions if q.emoji == superseasnail]:
        users = await reaction.users().flatten()
        for user in users:
            for p in a:
                if p[0] == user:
                    p[1] = True
        for c in a:
            if c[1]:
                if alerts not in c[0].roles:
                    await c[0].add_roles(alerts)
                    print(c[0], alerts, "+")
            else:
                if alerts in c[0].roles:
                    await c[0].remove_roles(alerts)
                    print(c[0], alerts, "-")
                

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
            
client.run(TOKEN)

    
