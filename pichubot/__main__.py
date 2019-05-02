# -*- coding: utf-8 -*-
"""Main driver to start bot."""

import os

from dotenv import load_dotenv
from pichubot import PichuBot

load_dotenv()

TOKEN = os.environ['PICHU_TOKEN']

def start_bot():
    """Start Pichu bot."""
    bot = PichuBot()
    bot.start(TOKEN)

if __name__ == '__main__':
    start_bot()
