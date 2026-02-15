from PURVIMUSIC import app
from pyrogram import filters, enums
from pyrogram.types import Message
from datetime import datetime
afk_users = {}
@app.on_message(filters.command("afk") & filters.group)
async def afk_command(client, message: Message):
    afk_users[message.from_user.id] = {"reason": message.text.split(None, 1)[1] if len(message.text.split()) > 1 else "AFK", "timestamp": datetime.now(), "first_name": message.from_user.first_name}
    await message.reply(f"✨ {message.from_user.first_name} is now AFK\n📝 Reason: {afk_users[message.from_user.id]['reason']}")
@app.on_message(filters.group & ~filters.service, group=1)
async def check_afk_status(client, message: Message):
    if message.from_user.id in afk_users:
        afk_data = afk_users.pop(message.from_user.id)
        await message.reply(f"🎉 Welcome back {message.from_user.first_name}!\n⌛ You were AFK for {int((datetime.now() - afk_data['timestamp']).total_seconds() / 60)} minute(s).\n📝 AFK Reason: {afk_data['reason']}")
    if message.reply_to_message and message.reply_to_message.from_user.id in afk_users:
        afk_data = afk_users[message.reply_to_message.from_user.id]
        await message.reply(f"💤 {afk_data['first_name']} is AFK\n📝 Reason: {afk_data['reason']}", quote=True)
