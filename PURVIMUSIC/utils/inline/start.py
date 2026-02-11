from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from PURVIMUSIC import app

# Replace this with your emoji ID
CUSTOM_EMOJI_ID = "5219943216781995020"


def start_panel(_):
    buttons = [
        [
            # Raw dict with icon_custom_emoji_id
            {
                "text": _["S_B_1"],
                "icon_custom_emoji_id": CUSTOM_EMOJI_ID,
                "url": f"https://t.me/{app.username}?startgroup=true"
            },
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    # Wrap raw dicts into InlineKeyboardButton via InlineKeyboardMarkup
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(**buttons[0][0]),
                buttons[0][1]
            ]
        ]
    )


def private_panel(_):
    buttons = [
        [
            {
                "text": _["S_B_10"],
                "icon_custom_emoji_id": CUSTOM_EMOJI_ID,
                "url": f"https://t.me/{app.username}?startgroup=true"
            }
        ],
        [
            InlineKeyboardButton(text=_["S_B_11"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_12"], callback_data="abot_cb"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="ubot_cb"),
        ],
    ]

    # Rebuild rows manually
    keyboard = []
    for row in buttons:
        new_row = []
        for btn in row:
            if isinstance(btn, dict):
                new_row.append(InlineKeyboardButton(**btn))
            else:
                new_row.append(btn)
        keyboard.append(new_row)

    return InlineKeyboardMarkup(keyboard)
    
