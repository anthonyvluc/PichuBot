"""Loads events for the Discord bot.


"""
def load_discord_events(bot):
  @bot.event
  async def on_ready():
    print('Pichu joins the battle!')

  # @bot.event
  # async def on_message(message):
  #   print('The message content was', message.content)
