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

@app.on_message(filters.command("afk"))
async def active_afk(_, message: Message):
    if message.sender_chat: return
    user_id = message.from_user.id
    if user_id in AFK_DB:
        data = AFK_DB.pop(user_id)
        time_away = get_readable_time(int(time.time() - data["time"]))
        await message.reply_text(f"**{message.from_user.first_name}** is back online! Away for {time_away}" + (f"\nReason: {data['reason']}" if data.get('reason') else ""))
        return
    
    details = {"time": time.time(), "reason": None}
    if len(message.command) > 1:
        details["reason"] = message.text.split(None, 1)[1].strip()[:100]
    
    AFK_DB[user_id] = details
    await message.reply_text(f"{message.from_user.first_name} is now AFK!" + (f"\nReason: {details['reason']}" if details['reason'] else ""))
