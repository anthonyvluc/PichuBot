#!/usr/bin/env python3

from pichu_bot import PICHU_BOT

def start_bot():
  bot = PICHU_BOT()
  bot.load_commands()
  bot.load_events()
  bot.start()

if __name__ == '__main__':
  start_bot()
