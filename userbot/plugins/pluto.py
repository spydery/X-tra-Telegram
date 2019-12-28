# (c) @UniBorg
# Original written by @UniBorg edit by @I_m_Rock

from telethon import events
import asyncio
from collections import deque


@borg.on(events.NewMessage(pattern=r"\.pluto", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🕐😬🕜😖🕑🥴🕝☠️🕛☠️🕔☠️🕒🕞🕓"))
	for _ in range(78):
		await asyncio.sleep(0.2)
		await event.edit("".join(deq))
		deq.rotate(4)
