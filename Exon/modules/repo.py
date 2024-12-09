# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @AshokShau
#     MY ALL BOTS :- Abishnoi_bots
#     GITHUB :- KingAbishnoi ""

from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from Exon import Abishnoi as pbot

blue = "https://telegra.ph/file/78fbd9d73e1f456857222.jpg"


@pbot.on_cmd("repo")
async def repo(_, message):
    await message.reply_photo(
        photo=blue,
        caption=f"""𝗥𝗲𝗽𝗼𝘀𝗶𝘁𝗼𝗿𝘆.
             [𝐁lue.](https://t.me/zavril)
             Heroku 1bulan 40K.
             Deploy repository 𝗕𝗹𝘂𝗲𝗳𝗹𝗼𝘆𝗱-Userbot dibawah!
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Deploy", url="https://dashboard.heroku.com/new?template=https://github.com/bluefloyd24/Kazu-Userbot"
                    ),
                    InlineKeyboardButton(
                        "Ask", url="https://t.me/zavril"
                    ),
                ]
            ]
        ),
    )
