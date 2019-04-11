import commands as cmds
from events import load_discord_events
from discord.ext import commands
import os

PREFIX = '!'
TOKEN = os.environ['PICHU_TOKEN']

"""Defines the PichuBot class.


"""
class PichuBot():
    def __init__(self):
        self.bot = commands.Bot(command_prefix=PREFIX)

    def start(self):
        print('Starting bot...')
        self.bot.run(TOKEN)

    def load_commands(self):
        # TODO: debug the commands not working
        print('Loading commands...')
        bot_cmds = [cmd for _, cmd in cmds.__dict__.items() if isinstance(cmd, commands.core.Command)]
        for cmd in bot_cmds:
            self.bot.add_command(cmd)

    def add_command(self, cmd):
        self.bot.add_command(cmd)

    def load_events(self):
        load_discord_events(self.bot)
