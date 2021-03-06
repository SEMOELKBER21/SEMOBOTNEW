from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.veez import user
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""๐ค **ุงูููููุง {message.from_user.mention()} ๐ค**\n
๐ค [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **ูุฐุง ุจูุช ุชุดุบูู ุงูููุณููู ูุงูููุฏูู ูู ูุฌููุนุงุช ูู ุฎูุงู ูุญุงุฏุซุงุช ุงูููุฏูู ุงูุฌุฏูุฏุฉ ูู ุงูุชูุฌูุฑุงู!**

๐ค **ุงูุชุดู ุฌููุน ุฃูุงูุฑ ุงูุฑูุจูุช ูููููุฉ ุนูููุง ูู ุฎูุงู ุงูููุฑ ุนูู ุฒุฑ ุงูุฃูุงูุฑ๐ค!**

๐ค **ููุนุฑูุฉ ููููุฉ ุงุณุชุฎุฏุงู ูุฐุง ุงูุฑูุจูุช ุ ุงูุฑุฌุงุก ุงูููุฑ ููู ุงูุฒุฑ ยปโ ุงูุฏููู ุงูุฃุณุงุณู!**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ ุถููููููู ุงูุจููููุช ููููููุฌูุนููุชู โ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(" ๐คุฏูููููู ุงูุงุณููุงุณููู๐ค", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("๐คุงูุงููุฑ๐ค", callback_data="cbcmds"),
                    InlineKeyboardButton("๐คุงูููููููุทูููุฑ๐ค", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "๐คุฌููุฑูุจ ุงูุชูููููุงุตู๐ค", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "๐คูููููุงู ุงูุชูููุญูุฏูุซุงุช๐ค", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "๐ค๐๐๐๐ ๐๐๐๐๐๐!!๐ค", url="https://t.me/S_E_M_O_E_L_K_B_E_R"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("๐คุฌููููุฑูุจ ุงูููููุชูุงุตููู๐ค", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "๐คููููููุงู ุงูุชุญูุฏูููุซุงุช๐ค", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**ูููููุฑุช {message.from_user.mention()}, ุงููููุง {BOT_NAME}**\n\n๐ค ููููุนููููููู ุงูููุจููููุช ุจููุดูููููููู ุทูููุจูููููุนููู\nุงุณูููุชููุงุฐ: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n๐ค ูุณุฎู ุงูุจูุช: `v{__version__}`\n๐ค ูููุณููุฎููู ุจูููุชูููุฌููุฑู: `{pyrover}`\n๐คูุณุณุฎู ุจุงูุซูู: `{__python_version__}`\n๐ ุจูููุช ููุชุงุฐ: `{pytover.__version__}`\nโจ ุญุงููุฉ ุงูุจูุช: `{uptime}`\n\n**ุดูุฑูุง ูุฅุถุงูุชู ููุง ุ ูุชุดุบูู ุงูููุฏูู ูุงูููุณููู ุนูู ุฏุฑุฏุดุฉ ุงูููุฏูู ุงูุฎุงุตุฉ ุจูุฌููุนุชู** โค"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("๐ค `ูููููููุฏ ุขูุชูููุดูุบูู`\n" f"๐ค `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "๐ค ุญููุขูููู ุขููููุจููุคุช:\n"
        f"โข **uptime:** `{uptime}`\n"
        f"โข **start time:** `{START_TIME_ISO}`"
    )


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "๐ค **ุดูุฑุง ูุฅุถุงูุชู ุฅูู ุงููุฌููุนุฉ !๐ค**\n\n"
                "**ุงูููุง ุจูููุช ูุชููุดููุบููู ุงูููุณููู ูุงููุฏูููุงุช ูู ุงููุญุงุฏุซู ุงูุตูุงุชูุฉ ูุงูุถูุงู ุงูุญุณุงุจ ุงููุณุงุนุฏ ูู ุจูุชุงุจู /userbotjoin ูุณุณูู ููุถู ุชููุงุฆู ููุงู ุงูุณูุฑุณ @SE_MO_1.**\n\n"
                "**Once done, type** /reload",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("๐คูููููููุงู ุงูููุจููุช๐ค", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("๐คุฌููุฑูุจ ุงูููุฏุนุนู๐ค", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton("๐คุงูููุญููุณููุงุจ ุงููููููููุณููุงุนููุฏ๐ค", url=f"https://t.me/{ass_uname}")
                        ]
                    ]
                )
            )
