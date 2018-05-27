import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio, random, os, time#, psycopg2
import twitter

try:
    from config import TOKEN, TCK, TCS, TATC, TATS
except ModuleNotFoundError:
    TOKEN = os.environ["TOKEN"]
    TCK = os.environ["TCK"]
    TCS = os.environ["TCS"]
    TATC = os.environ["TATC"]
    TATS = os.environ["TATS"]


client = discord.Client()
prefix = "."
client = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(activity = discord.Game(name="Exclusively for 'Splat Hub!'"))
    await onlinestuff()

async def onlinestuff():
    global server, channnel, wiiu, switch, na, eu, naflag, euflag, wiiuflag, switchflag, person, message, roles, api
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
    api = twitter.Api(
        consumer_key=TCK,
        consumer_secret=TCS,
        access_token_key=TATC,
        access_token_secret=TATS)
    t = api.GetUserTimeline(screen_name="splatoon2maps", count=3)
    tweets = [i.AsDict() for i in t]
    print(tweets)   
        

    
    while True:
        await reactioncheck()


@client.group(pass_context=True)
async def stages(ctx):
    if ctx.invoked_subcommand == None:
        await ctx.send("""Available Modes:
```md
<.stages regular>
<.stages ranked>
<.stages league>```""")

@stages.command(pass_context=True)
async def regular(ctx):
    t = api.GetUserTimeline(screen_name="splatoon2maps", count=3)
    tweets = [i.AsDict() for i in t]
    for tweet in tweets:
        if "Turf War" in tweet["text"]:
            map1 = tweet["text"].split("Turf War maps: ")[1]
            map1 = map1.split(" &amp;")[0]
            map2 = tweet["text"].split("&amp; ")[1]
            map2 = map2.split(" #Splatoon2")[0]
            map1photo = tweet["media"][0]["media_url"]
            map2photo = tweet["media"][1]["media_url"]
            embed = discord.Embed(title = "Regular Battle", description="""
**Mode:**
Turf War

**Maps:**
{}
{}""".format(map1,map2),colour=0x19D619)
            await ctx.send(embed=embed)
            await ctx.send("{} {}".format(map1photo,map2photo))



@stages.command(pass_context=True)
async def ranked(ctx):
    t = api.GetUserTimeline(screen_name="splatoon2maps", count=3)
    tweets = [i.AsDict() for i in t]
    for tweet in tweets:
        if "Ranked Battle" in tweet["text"]:
            mode = tweet["text"].split("Ranked Battle maps — ")[1]
            mode = mode.split(": ")[0]
            map1 = tweet["text"].split(": ")[1]
            map1 = map1.split(" &amp;")[0]
            map2 = tweet["text"].split("&amp; ")[1]
            map2 = map2.split(" #Splatoon2")[0]
            map1photo = tweet["media"][0]["media_url"]
            map2photo = tweet["media"][1]["media_url"]
            embed = discord.Embed(title = "Ranked Battle", description="""
**Mode:**
{}

**Maps:**
{}
{}""".format(mode,map1,map2),colour=0xF44910)
            await ctx.send(embed=embed)
            await ctx.send("{} {}".format(map1photo,map2photo))

@stages.command(pass_context=True)
async def league(ctx):
    t = api.GetUserTimeline(screen_name="splatoon2maps", count=3)
    tweets = [i.AsDict() for i in t]
    for tweet in tweets:
        if "League Battle" in tweet["text"]:
            mode = tweet["text"].split("League Battle maps — ")[1]
            mode = mode.split(": ")[1]
            map1 = tweet["text"].split(": ")[1]
            map1 = map1.split(" &amp;")[0]
            map2 = tweet["text"].split("&amp; ")[1]
            map2 = map2.split(" #Splatoon2")[0]
            map1photo = tweet["media"][0]["media_url"]
            map2photo = tweet["media"][1]["media_url"]
            embed = discord.Embed(title = "League Battle", description="""
**Mode:**
{}

**Maps:**
{}
{}""".format(mode,map1,map2),colour=0xEE2D7C)
            await ctx.send(embed=embed)
            await ctx.send("{} {}".format(map1photo,map2photo))




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

    
