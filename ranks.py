import discord
from discord.ext import commands
import gsheets

class Ranks():


    def __init__(self, client):
        self.client = self.bot = client
        self.ranksss = gsheets.read()
        self.rankss = [x.split(" (")[0] for x in self.ranksss]
        self.rank_lower = {x.lower():x for x in self.rankss}

       
    
    @commands.command()
    async def rank(self, ctx, *, rank=None):
        if not rank: return await ctx.send(embed=discord.Embed(title="Ranks",description="\n".join(self.ranksss)))
        rank = rank.lower()
        if rank in self.rank_lower:
            rank = self.rank_lower[rank]
            role = discord.utils.get(ctx.guild.roles,name=rank)
            if role in ctx.author.roles:
                await ctx.author.remove_roles(role)
                await ctx.send(f"{ctx.author.mention}, you have been removed from the **{role.name}** role")
            else:
                 await ctx.author.add_roles(role)
                 await ctx.send(f"{ctx.author.mention}, you have been given the **{role.name}** role")
        else: await ctx.send("That's not a rank!")

    @commands.command()
    @commands.has_role("Agents")
    async def delrank(self, ctx, *, rank):
        rank = rank.lower()
        if rank in self.rank_lower:
            rank = self.rank_lower[rank]
            gsheets.delrank(rank)
            self.ranks.remove(rank)
            self.rankss.remove(rank)
            await ctx.send(f"{ctx.author.mention}, the rank has been removed")
        else: await ctx.send("That rank isn't on the list!")

    @commands.command()
    @commands.has_role("Agents")
    async def addrank(self, ctx, *, rank):
        if discord.utils.get(ctx.guild.roles, name=rank):
            gsheets.addrank(rank)
            self.rank.append(rank)
            self.rankss.remove(rank)
        else: await ctx.send("That rank isn't in the server! (Check case sensitivity)")


def setup(client):
    client.add_cog(Ranks(client))

            
