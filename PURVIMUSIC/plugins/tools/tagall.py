from PURVIMUSIC import app
from pyrogram import filters, enums
from pyrogram.types import Message

@app.on_message(filters.command("all") & filters.group)
async def tagall(client, message: Message):
    admins = [admin.user.id async for admin in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
    if message.from_user.id in admins:
        await message.reply(f"{' '.join([f'@{m.user.username}' if m.user.username else f'[{m.user.first_name}](tg://user?id={m.user.id})' async for m in client.get_chat_members(message.chat.id)])}\n\n{message.text.split(None, 1)[1] if len(message.text.split()) > 1 else ''}")
