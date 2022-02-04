from ..db import record
from ..src import bot


async def get_channel(guild_id: int):
    channel_id = await record('SELECT log_ch FROM channels WHERE guild_id = %s', guild_id)
    if channel_id:
        channel = bot.get_channel(channel_id)

        return channel
