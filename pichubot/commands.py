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
async def pichu(ctx):
    await ctx.send('Pichu pichu!')

"""test
Pichu is a parrot
Args:
    msg (str): passed in message
"""
@commands.command(pass_context=True)
async def echo(ctx, msg=None):
    if msg is not None:
        await ctx.send(msg)
    else:
        await ctx.send('Missing parameter!')
