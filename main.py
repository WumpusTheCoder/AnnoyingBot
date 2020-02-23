import os
import random
import math, sys, time

import ctx as ctx
from discord import *
from decimal import *
from discord.ext import commands

token = 'NjgwMTQ5ODQ5NTA4OTM3Nzgw.XlEnQQ.kAhDQ9AjQDbNtwD4rzzBHRdlzGc'
bot = commands.Bot(command_prefix='$')

print("Bot Online and Connected")


@bot.command(name='oof', help='oof the chat with an assigned amount of messages')
async def repeat(ctx, message, n: int):
    if n <= 100:
        for i in range(n):
            await ctx.send(message)
    else:
        await ctx.send(f"{n} is greater than the limit of 100!")
    await ctx.send(f"Completed {n} times.")


@bot.command(name='kill', help='Tries to stop ANY commands running any further.')
async def kill(ctx):
    await ctx.send("Trying to stop now.")
    killswitch = True

@bot.command(name='nuke', help='BREAKS DISCORD!')
async def nuke(ctx, killswitch=False):
    n: int
    n = 100000000000000000000000000000000000000000000000000000000
    if killswitch == False:
        if n <= 100000000000000000000000000000000000000000000000000000000:
            for i in range(n):
                await ctx.send("nuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke ")
        await ctx.send(f"If you see this, u survived somehow.")


@bot.command(name='test', help='A special command for testing made by Eli3Bear.')
async def test(ctx):
    await ctx.send("Trying to stop now.")
    await ctx.send("Trying to stop now.")
    await ctx.send("Trying to stop now.")
    await ctx.send("Trying to stop now.")
    await ctx.send("Trying to stop now.")
    await ctx.send("Trying to stop now.")
    await ctx.send("Trying to stop now.")


bot.run(token)
