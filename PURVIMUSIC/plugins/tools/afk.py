from PURVIMUSIC import app
from pyrogram import filters, enums
from pyrogram.types import Message

afk_users = {}

@app.on_message(filters.command("afk") & filters.group)
async def afk_command(client, message: Message):
    admins = [admin.user.id async for admin in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
    if message.from_user.id in admins:
        afk_users[message.from_user.id] = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else "AFK"
        await message.reply(f"{message.from_user.first_name} is now AFK: {afk_users[message.from_user.id]}")

@app.on_message(filters.group & filters.reply)
async def afk_trigger(client, message: Message):
    if message.reply_to_message and message.reply_to_message.from_user.id in afk_users:
        await message.reply(f"{message.reply_to_message.from_user.first_name} is AFK: {afk_users[message.reply_to_message.from_user.id]}")
