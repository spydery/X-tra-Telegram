""".admin Plugin for @XtraTgBot"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "♔彡[ i am 𝕮𝖍𝖊𝖆𝖕™ ]彡♔, check pinned in @opgohil"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`YO BRO JABTAK YE KHEL KHATAM NHI HOTA APUN IDHARICH HAI ψ(｀∇´)ψ`**\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\nfork by:` @opgohil\n`Database Status: Databases functioning normally!\n\nAlways with you, my master!\n`"
                     f"`My peru owner`: {DEFAULTUSER}\n"
                     "[Deploy this userbot Now](https://github.com/Dark-Princ3/X-tra-Telegram)")
