from telegram import InlineKeyboardButton, InlineKeyboardMarkup

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


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=f'<emoji id="5219943216781995020">⚡️</emoji>', url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons





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
