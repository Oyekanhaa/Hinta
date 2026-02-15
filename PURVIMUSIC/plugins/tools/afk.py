from PURVIMUSIC import app
from pyrogram import filters, enums
from pyrogram.types import Message
from datetime import datetime

afk_users = {}

@app.on_message(filters.command("afk") & filters.group)
async def afk_command(client, message: Message):
    user_id = message.from_user.id
    
    # Check if user is admin (optional, remove if you want all users to use AFK)
    admins = [admin.user.id async for admin in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
    
    # Store AFK status with timestamp
    reason = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else "AFK"
    afk_users[user_id] = {
        "reason": reason,
        "timestamp": datetime.now(),
        "first_name": message.from_user.first_name
    }
    
    await message.reply(f"✨ **{message.from_user.first_name} is now AFK**\n📝 **Reason:** {reason}")

@app.on_message(filters.group & ~filters.service, group=1)
async def check_afk_status(client, message: Message):
    user_id = message.from_user.id
    
    # Check if user is AFK and just returned
    if user_id in afk_users:
        afk_data = afk_users.pop(user_id)  # Remove from AFK
        afk_duration = datetime.now() - afk_data["timestamp"]
        minutes = int(afk_duration.total_seconds() / 60)
        
        await message.reply(
            f"🎉 **Welcome back {message.from_user.first_name}!**\n"
            f"⌛ You were AFK for {minutes} minute(s).\n"
            f"📝 AFK Reason: {afk_data['reason']}"
        )
    
    # Check if message mentions/replies to an AFK user
    else:
        # Check for mentions in text
        if message.text:
            for user_id in list(afk_users.keys()):
                if f"@{message.from_user.username}" in message.text and user_id != message.from_user.id:
                    afk_data = afk_users[user_id]
                    await message.reply(
                        f"💤 **{afk_data['first_name']} is AFK**\n"
                        f"📝 **Reason:** {afk_data['reason']}"
                    )
        
        # Check for replied message
        if message.reply_to_message and message.reply_to_message.from_user.id in afk_users:
            replied_user_id = message.reply_to_message.from_user.id
            afk_data = afk_users[replied_user_id]
            await message.reply(
                f"💤 **{afk_data['first_name']} is AFK**\n"
                f"📝 **Reason:** {afk_data['reason']}"
            )
