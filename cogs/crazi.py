# Commands for The Crazi Rally (2018)

import discord
from discord.ext import commands


class The_Crazi_Rally():
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def pcmasterrace(self, ctx):  # Joke commands
        """Consoles are better than PCs!"""
        await self.client.say(ctx.message.author.mention + " Joined the dark side!! SUCK IT CONSOLE PEASANTS!!")

    @commands.command(pass_context=True)
    async def consolemasterrace(self, ctx):  # Joke commands
        """PCs are better than consoles!"""
        await self.client.say(ctx.message.author.mention + " Is just plain stupid.")

    @commands.command(pass_context=True, aliases=['harvey'])
    async def harvster(self, ctx):  # Harvey's command
        """Harvey's command"""
        await self.client.say("**Harvey is my hero!**")

    @commands.command(pass_context=True)
    async def sharkira(self, ctx):  # Harvey's command
        """SHARK-IRA SHARK-IRA"""
        await self.client.say(ctx.message.author.mention + " https://youtu.be/fdfUd9Mc__g")


def setup(client):
    client.add_cog(The_Crazi_Rally(client))
