# -*- coding: utf-8 -*-
"""Defines commands for the Discord bot.

Each function is its own command.

"""

from discord.ext import commands

"""test

TODO
"""
@commands.command(pass_context=True)
async def test(ctx, arg):
    print(dir(ctx))
    await ctx.send(arg)

"""test

TODO
"""
# @commands.command(pass_context=True)
# async def test2():
#     pass


