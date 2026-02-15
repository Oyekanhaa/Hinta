from PURVIMUSIC import app
from pyrogram import filters, enums
from pyrogram.types import Message

@app.on_message(filters.command("all") & filters.group)
async def tagall(client, message: Message):
    admins = [admin.user.id async for admin in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
    if message.from_user.id not in admins: return await message.reply("Only admins can use this command")
    members = [f"[{m.user.first_name}](tg://user?id={m.user.id})" async for m in app.get_chat_members(message.chat.id) if not m.user.is_bot]
    text = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else ""
    await message.reply(f"{' '.join(members)}\n\n{text}")
