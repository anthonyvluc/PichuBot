# -*- coding: utf-8 -*-
"""Defines commands for the Discord bot.

Each function is its own command.

"""

from __future__ import print_function

from discord.ext import commands

"""pichu

Say something Pichu!

"""
@commands.command(pass_context=True)
async def pichu(ctx, arg=None):
    if arg is not None:
        await ctx.send(arg)
    else:
        await ctx.send('Missing parameter!')

"""test

TODO
"""
# @commands.command(pass_context=True)
# async def test2():
#     pass


