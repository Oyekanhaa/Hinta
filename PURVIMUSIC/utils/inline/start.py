from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton

import config
from PURVIMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_['S_B_1'], 
                url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id="5310169226856644648",
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
