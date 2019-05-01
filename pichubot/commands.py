# -*- coding: utf-8 -*-
"""Defines commands for the Discord bot.

Each function is its own command.

"""

from __future__ import print_function

from random import randrange

from discord.ext import commands

"""pichu

Say something Pichu!

"""
@commands.command(pass_context=True)
async def pichu(ctx):
    await ctx.send('Pichu pichu!')

"""echo

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

"""roll

Roll a dice

Args:
    sides (str): passed in number of sides

"""
@commands.command(pass_context=True)
async def roll(ctx, sides=None):
    if sides is None:
        sides = 6
    # TODO: no handling of user error if sides is a word not number
    # maybe abstract an exception catcher
    await ctx.send(randrange(int(sides))+1)
