#!/usr/bin/env python3

from pichubot import PichuBot

def start_bot():
  bot = PichuBot()
  bot.load_commands()
  bot.load_events()
  bot.start()

if __name__ == '__main__':
  start_bot()
