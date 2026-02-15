import time
from pyrogram import filters
from pyrogram.types import Message
from PURVIMUSIC import app

AFK_DB = {}

def get_readable_time(seconds):
    periods = [('day', 86400), ('hour', 3600), ('minute', 60), ('second', 1)]
    result = []
    for period_name, period_seconds in periods:
        if seconds >= period_seconds:
            period_value, seconds = divmod(seconds, period_seconds)
            result.append(f"{int(period_value)} {period_name}{'s' if period_value > 1 else ''}")
    return ', '.join(result) if result else '0 seconds'

@app.on_message(filters.command(["afk"]))
async def active_afk(_, message: Message):
    if message.sender_chat: return
    user_id = message.from_user.id
    if user_id in AFK_DB:
        data = AFK_DB.pop(user_id)
        time_away = get_readable_time(int(time.time() - data["time"]))
        await message.reply_text(f"**{message.from_user.mention}** is back online! Away for {time_away}" + (f"\nReason: {data['reason']}" if data.get('reason') else ""))
        return
    
    AFK_DB[user_id] = {"time": time.time(), "reason": message.text.split(None, 1)[1].strip()[:100] if len(message.command) > 1 else None}
    await message.reply_text(f"{message.from_user.mention} is now AFK!" + (f"\nReason: {AFK_DB[user_id]['reason']}" if AFK_DB[user_id]['reason'] else ""))

@app.on_message(filters.text & filters.private | filters.group, group=1)
async def check_afk(_, message: Message):
    if message.sender_chat or not message.from_user: return
    user_id = message.from_user.id
    if user_id in AFK_DB and message.text and not message.text.startswith("/afk"):
        data = AFK_DB.pop(user_id)
        time_away = get_readable_time(int(time.time() - data["time"]))
        await message.reply_text(f"**{message.from_user.mention}** is back online! Away for {time_away}" + (f"\nReason: {data['reason']}" if data.get('reason') else ""))
