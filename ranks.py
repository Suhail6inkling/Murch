import discord
from discord.ext import commands
import gsheets

class Ranks():


    def __init__(self, client):
        self.client = self.bot = client
        self.ranks = gsheets.read()
        self.rankss = [x.split(" (")[0] for x in self.ranks]

    @commands.command()
    async def ranks(self, ctx):
        await ctx.send(embed=discord.Embed(title="Ranks",description="\n".join(self.ranks)))
    
    @commands.command()
    async def rank(self, ctx, *, rank):
        if rank in self.rankss:
            await ctx.author.add_roles(discord.utils.get(ctx.guild.roles,name=rank))

    @commands.command()
    @commands.has_role("Off the Hookers")
    async def delrank(self, ctx, *, rank):
        if rank in self.rankss:
            gsheets.delrank(rank)
            self.ranks.remove(rank)
            self.rankss.remove(rank)

    @commands.command()
    @commands.has_role("Off the Hookers")
    async def addrank(self, ctx, *, rank):
        if discord.utils.get(ctx.guild.roles, name=rank):
            gsheets.addrank(rank)
            self.rank.append(rank)
            self.rankss.remove(rank)


def setup(client):
    client.load_extension(Ranks(client))

            
