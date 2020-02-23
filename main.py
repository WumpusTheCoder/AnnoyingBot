import os
import random
import math, sys, time
import ctx as ctx
from discord import *
from decimal import *
from discord.ext import commands

token = 'Your Bot Token here in Speechmarks'
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


@bot.command(name='nuke', help='BREAKS DISCORD!')
async def nuke(ctx):
    n: int
    n = 100000000000000000000000000000000000000000000000000000000
       if n <= 100000000000000000000000000000000000000000000000000000000:
           for i in range(n):
               await ctx.send("nuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke \nnuke ")
       await ctx.send(f"If you see this, u survived somehow.")


bot.run(token)
