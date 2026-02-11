from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    ABUTTON = [[InlineKeyboardButton("˹ sᴜᴘᴘᴏꝛᴛ ˼", url="https://t.me/kanhaxduniya")],[InlineKeyboardButton("˹ ᴜᴘᴅᴧᴛᴇ ˼", url="https://t.me/About_kanhaa"),
    InlineKeyboardButton("˹ ᴧʟʟ ʙᴏᴛ ˼", url="https://t.me/About_kanha")],[InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data=f"settingsback_helper"),
    ]]

    UBUTTON = [[InlineKeyboardButton("˹ ᴍᴜsɪᴄ ˼", callback_data="settings_back_helper"),InlineKeyboardButton("˹ ᴛᴏᴏʟs ˼", callback_data=f"mbot_cb")],[InlineKeyboardButton("˹ ᴍᴧɴᴧɢᴇ ˼", callback_data=f"bbot_cb"),
    InlineKeyboardButton("˹ ʀᴧɪᴅ ˼", callback_data="cplus HELP_raid")],[InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data=f"settingsback_helper"),
    ]]
