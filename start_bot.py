#!/usr/bin/env python3
"""Main driver to start bot."""

from pichubot.pichubot import PichuBot

def start_bot():
    """Start Pichu bot."""
    bot = PichuBot()
    bot.start()

if __name__ == '__main__':
    start_bot()
