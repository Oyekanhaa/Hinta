from PURVIMUSIC import app
from pyrogram import filters
from pyrogram.types import Message
from datetime import datetime

afk_users = {}

@app.on_message(filters.command("afk") & filters.group)
async def afk_command(client, message: Message):
    reason = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else "AFK"
    afk_users[message.from_user.id] = {
        "reason": reason,
        "time": datetime.now(),
        "name": message.from_user.first_name
    }
    await message.reply(f"✨ {message.from_user.first_name} is now AFK\n📝 Reason: {reason}")

@app.on_message(filters.group & ~filters.service)
async def check_afk(client, message: Message):
    user_id = message.from_user.id
    
    # Check if user is returning from AFK
    if user_id in afk_users:
        data = afk_users.pop(user_id)
        minutes = int((datetime.now() - data["time"]).total_seconds() / 60)
        await message.reply(f"🎉 Welcome back {message.from_user.first_name}!\n⌛ AFK: {minutes}m\n📝 Reason: {data['reason']}")
        return
    
    # Check if replying to an AFK user
    if message.reply_to_message:
        replied_id = message.reply_to_message.from_user.id
        if replied_id in afk_users:
            data = afk_users[replied_id]
            await message.reply(f"💤 {data['name']} is AFK\n📝 Reason: {data['reason']}", quote=True)
