# plugin by lejend @Kraken_The_Badass
"""Emoji

Available Commands:

.lucky"""

from telethon import events

import asyncio
from uniborg.util import admin_cmd




@borg.on(admin_cmd(pattern="lucky"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 17)

    #input_str = event.pattern_match.group(1)

    #if input_str == "lucky":

    await event.edit("Lucky...š¤š¤")

    animation_chars = [
        
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬[š](https://t.me/MAFIA_USERBOT)ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nšā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬[š](https://t.me/MAFIA_USERBOT)ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬šā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬[š](https://t.me/MAFIA_USERBOT)ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬šā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬[š](https://t.me/MAFIA_USERBOT)ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬šā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬[š](https://t.me/MAFIA_USERBOT)ā¬",    
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬šā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬[š](https://t.me/MAFIA_USERBOT)ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬šā¬\nā¬ā¬ā¬[š](https://t.me/MAFIA_USERBOT)ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬šā¬\nā¬ā¬ā¬[š](https://t.me/MAFIA_USERBOT)ā¬\nā¬ā¬ā¬ā¬ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬šā¬\nā¬ā¬ā¬[š](https://t.me/MAFIA_USERBOT)ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬šā¬ā¬\nā¬ā¬[š](https://t.me/MAFIA_USERBOT)ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬šā¬ā¬ā¬\nā¬[š](https://t.me/MAFIA_USERBOT)ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nšā¬ā¬ā¬ā¬\n[š](https://t.me/MAFIA_USERBOT)ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬",
            "ā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬ā¬",
            "ā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬\nā¬ā¬ā¬ā¬",
            "ā¬ā¬ā¬\nā¬ā¬ā¬\nā¬ā¬ā¬",
            "ā¬ā¬\nā¬ā¬",
            "[ššš»Ye le gift](https://t.me/MAFIA_USERBOT)"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 17])
