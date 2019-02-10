import commands as aaa_cmds
from events import load_discord_events
from discord.ext import commands
import os

PREFIX = '!'
TOKEN = os.environ['PICHU_TOKEN']

"""Defines the AAA Bot class.


"""
class AAA_BOT():
  def __init__(self):
    self.bot = commands.Bot(command_prefix=PREFIX)

  def start(self):
    print('Starting bot...')
    self.bot.run(TOKEN)

  def load_commands(self):
    # TODO: debug the commands not working
    print('Loading commands...')
    cmds = [c for _, c in aaa_cmds.__dict__.items() if isinstance(c, commands.core.Command)]
    for c in cmds:
      self.bot.add_command(c)

  def add_command(self, c):
    self.bot.add_command(c)

  def load_events(self):
    load_discord_events(self.bot)