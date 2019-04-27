# -*- coding: utf-8 -*-
"""Defines the PichuBot class.

This bot loads commands from a subdirectory which can be invoked with `!`.

"""

from __future__ import print_function
import os

import commands as cmds
from discord.ext import commands
from events import load_discord_events

PREFIX = '!'
TOKEN = os.environ['PICHU_TOKEN']


class PichuBot(object):
    """The PichuBot class."""

    def __init__(self):
        """Defines the initialization."""
        self.bot = commands.Bot(command_prefix=PREFIX)

    def start(self):
        """Defines the startup."""
        print('Starting bot...')
        self._load_commands()
        self._load_events()
        self.bot.run(TOKEN)

    def _load_commands(self, directory=None):
        """Loads bot commands from a given directory.

        Iterates through the files of a given directory and loads them as
        custom commands.

        Args:
            directory (str): directory's name of command files

        """
        # TODO: load from directory of command files
        print('Loading commands...')
        bot_cmds = [cmd for _, cmd in cmds.__dict__.items()
                    if isinstance(cmd, commands.core.Command)]
        for cmd in bot_cmds:
            self.bot.add_command(cmd)

    def _load_events(self, directory=None):
        """Loads bot events from a given directory."""
        load_discord_events(self.bot)
