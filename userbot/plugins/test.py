    
#Credit To @Kraken_The_BadASS . Keep credit if you are going to edit it. Join @HellBot_Official


import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="test ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
       
        await event.edit("`Testing ππΈπ½ππΈ πππΌβπΉππ....`")
        await asyncio.sleep(2)
        await event.edit("`Testing ππΈπ½ππΈ πππΌβπΉππ..`")
        await asyncio.sleep(2)
        await event.edit("__Testing Successful__")
        await asyncio.sleep(2)
        await event.edit("`Making Output` \n\nPlease wait")
        await asyncio.sleep(2)
        await event.edit("__Output Successful__")
        await asyncio.sleep(3.5)
        await event.edit("Your[ππΈπ½ππΈ πππΌβπΉππ](https://t.me/MAFIA_USERBOT) is working Fine...\n       Join @MAFIA_USERBOT For Any Help......")
