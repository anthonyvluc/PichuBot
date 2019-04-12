# -*- coding: utf-8 -*-
"""Loads events for the Discord bot.

Given a Discord bot class, override these events.

"""
def load_discord_events(bot):
    @bot.event
    async def on_ready():
        print('Pichu joins the battle!')
