#!/usr/bin/env python3

from aaa_bot import AAA_BOT

def start_bot():
  bot = AAA_BOT()
  bot.load_commands()
  bot.load_events()
  bot.start()

if __name__ == '__main__':
  start_bot()
