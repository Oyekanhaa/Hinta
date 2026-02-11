from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def start_panel(update, context):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Invite 🤙",
                    url=config.SUPPORT_CHAT,
                    api_kwargs={"icon_custom_emoji_id": "5219943216781995020"}
                ),
            ]
        ]
    )

    await update.message.reply_text(
        "Click below!",
        reply_markup=keyboard
    )
    


from pyrogram.types import InlineKeyboardButton

import config
from PURVIMUSIC import app








def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_10"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_11"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_12"], callback_data=f"abot_cb"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data=f"ubot_cb"),
        ],
    ]
    return buttons
