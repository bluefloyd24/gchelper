"""
MIT License

Copyright (c) 2022 AshokShau

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @AshokShau
#     UPDATE   :- Abishnoi_bots
#     GITHUB :- AshokShau ""

from pyrogram.types import CallbackQuery
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CallbackQueryHandler

from Exon import Abishnoi as pbot
from Exon import BOT_NAME, OWNER_ID, OWNER_USERNAME, SUPPORT_CHAT
from Exon import dispatcher


@pbot.on_callback_query()
async def close(Client, cb: CallbackQuery):
    if cb.data == "close2":
        await cb.answer()
        await cb.message.delete()


# CALLBACKS


def ABG_about_callback(update, context):
    query = update.callback_query
    if query.data == "ABG_":
        query.message.edit_text(
            text=f"๏ Gue {BOT_NAME} , lu pada bisa pake gua buat ngatur grup lu biar ga ribet"
                 "\n•  buat mantau user yang dibatesin"
                 "\n•  bisa bikin welkam meseg buat yang baru dateng, trus bisa buat atutan grup"
                 "\n•  gue ini keren pokoknya, anti banjir kalo bahasa org tele"
                 "\n•  gue bisa nganuin member yang ngeyel, ban kik mute apalah pokoknya bisak"
                 "\n•  gua punya beberapa note buat blacklist, nyimpen setting, sama beberapa perintah"
                 "\n•  sebelom lu nyuruh gue, gue liat dulu grup lu ngasih akses buat gua kaga"
                 "\n\n_Gue udah punya lisensi yang akurat dah pokoknya di tele"
                 "\n\n*Pencet aja kalo kepo sama gueeheheheehe*.",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="𝗔𝗱𝗺𝗶𝗻", callback_data="ABG_admin"),
                        InlineKeyboardButton(text="𝗡𝗼𝘁𝗲𝘀", callback_data="ABG_notes"),
                    ],
                    [
                        InlineKeyboardButton(
                            text="𝗦𝘂𝗽𝗽𝗼𝗿𝘁", callback_data="ABG_support"
                        ),
                        InlineKeyboardButton(
                            text="𝗖𝗿𝗲𝗱𝗶𝘁", callback_data="ABG_credit"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="𝗦𝗼𝘂𝗿𝗰𝗲",
                            callback_data="source_",
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="𝗕𝗮𝗹𝗶𝗸", callback_data="start_back"
                        ),
                    ],
                ]
            ),
        )

    elif query.data == "ABG_admin":
        query.message.edit_text(
            text=f"━━━━━━━ *ᴀᴅᴍɪɴ* ━━━━━━━\nʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴛʜᴇ 𝙼ᴜsɪᴄ ᴍᴏᴅᴜʟᴇ\n⍟*ᴀᴅᴍɪɴ*\nᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs\n/pause /n»ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ.\n/resume\n» ʀᴇsᴜᴍᴇᴅ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ.\n/skip ᴏʀ /next\n»sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ.\n/end ᴏʀ /stop\n» ᴇɴᴅ ᴛʜᴇ ᴄᴜʀᴇᴇɴᴛ ᴏɴɢᴏɪɴ sᴛʀᴇᴀᴍ.\n⍟*ᴀᴜᴛʜ*\nᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴀᴜᴛʜ/ᴜɴᴀᴜᴛʜ ᴀɴʏ ᴜsᴇʀ\n• ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ᴄᴀɴ sᴋɪᴩ, ᴩᴀᴜsᴇ, ʀᴇsᴜᴍᴇ ᴀɴᴅ ᴇɴᴅ ᴛʜᴇ sᴛʀᴇᴀᴍ ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ʀɪɢʜᴛs./n/auth ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ\n» ᴀᴅᴅ ᴀ ᴜsᴇʀ ᴛᴏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.\n/unauth ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ \n» ʀᴇᴍᴏᴠᴇs ᴛʜᴇ ᴜsᴇʀ ғʀᴏᴍ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛ.\n/authusers \n» sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.\n⍟*ᴘʟᴀʏ*\nᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴩʟᴀʏ sᴏɴɢs\n/play <sᴏɴɢ ɴᴀᴍᴇ/ʏᴛ ᴜʀʟ>\n» sᴛᴀʀᴛs ᴩʟᴀʏɪɴɢ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ sᴏɴɢ ᴏɴ ᴠᴄ.!",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="👻", callback_data="start_back"),
                        InlineKeyboardButton(text="🚀️", callback_data="AsuX_help"),
                        InlineKeyboardButton(text="💵", callback_data="ABG_credit"),
                        InlineKeyboardButton(text="📎️", callback_data="source_"),
                        InlineKeyboardButton(text="⬅️️", callback_data="help_back"),
                    ]
                ]
            ),
        )

    elif query.data == "ABG_notes":
        query.message.edit_text(
            text=f"<b>๏ sᴇᴛᴛɪɴɢ ᴜᴘ ɴᴏᴛᴇs</b>"
                 f"\nʏᴏᴜ ᴄᴀɴ sᴀᴠᴇ ᴍᴇssᴀɢᴇ/ᴍᴇᴅɪᴀ/ᴀᴜᴅɪᴏ ᴏʀ ᴀɴʏᴛʜɪɴɢ ᴀs ɴᴏᴛᴇs"
                 f"\nᴛᴏ ɢᴇᴛ ᴀ ɴᴏᴛᴇ sɪᴍᴘʟʏ ᴜsᴇ # ᴀᴛ ᴛʜᴇ ʙᴇɢɪɴɴɪɴɢ ᴏғ ᴀ ᴡᴏʀᴅ"
                 f"\n\nʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ sᴇᴛ ʙᴜᴛᴛᴏɴs ғᴏʀ ɴᴏᴛᴇs ᴀɴᴅ ғɪʟᴛᴇʀs (ʀᴇғᴇʀ ʜᴇʟᴘ ᴍᴇɴᴜ)",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="𝗕𝗮𝗹𝗶𝗸", callback_data="ABG_")]]
            ),
        )
    elif query.data == "ABG_support":
        query.message.edit_text(
            text=f"*๏ {BOT_NAME} sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛs*"
                 "\nᴊᴏɪɴ ᴍʏ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ғᴏʀ sᴇᴇ ᴏʀ ʀᴇᴘᴏʀᴛ ᴀ ᴘʀᴏʙʟᴇᴍ ᴏɴ BLUE",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url=f"t.me/{SUPPORT_CHAT}"
                        ),
                        InlineKeyboardButton(
                            text="𝗨𝗽𝗱𝗮𝘁𝗲", url="https://t.me/yzigot"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="𝗕𝗮𝗹𝗶𝗸", callback_data="ABG_"),
                    ],
                ]
            ),
        )

    elif query.data == "ABG_credit":  # Credit  i hope edit nai hoga
        query.message.edit_text(
            text=f"━━━━━━━ *ᴄʀᴇᴅɪᴛ* ━━━━━━━"
                 "\n🛡️ *ᴄʀᴇᴅɪᴛ ꜰᴏʀ 𝗕𝗟𝗨𝗘 𝗥𝗢𝗕𝗢𝗧* 🛡️"
                 "\n\nʜᴇʀᴇ ɪꜱ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴀɴᴅ"
                 f"\nꜱᴘᴏɴꜱᴏʀ ᴏꜰ [{BOT_NAME}](t.me/bluehelp_bot)"
                 "\n\nʜᴇ ꜱᴘᴇɴᴛ ᴀ ʟᴏᴛ ᴏꜰ ᴛɪᴍᴇ ꜰᴏʀ"
                 f"\nᴍᴀᴋɪɴɢ [{BOT_NAME}](t.me/{OWNER_USERNAME}) ᴀ"
                 "\nꜱᴜᴘᴇʀ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="👻", callback_data="start_back"),
                        InlineKeyboardButton(text="🚀️", callback_data="ABG_admin"),
                        InlineKeyboardButton(text="💵", callback_data="AsuX_help"),
                        InlineKeyboardButton(text="📎‍", callback_data="source_"),
                        InlineKeyboardButton(text="⬅️️", callback_data="help_back"),
                    ],
                    [
                        InlineKeyboardButton(
                            text="𝗕𝗹𝘂𝗲'𝘀", url="https://t.me/proofniyeee"
                        ),
                        InlineKeyboardButton(
                            text="𝗖𝗵𝗮𝘁", url=f"https://t.me/{SUPPORT_CHAT}"
                        ),
                    ],
                ]
            ),
        )


def Source_about_callback(update, context):
    query = update.callback_query
    if query.data == "source_":
        query.message.edit_text(
            text=f"""
*ʜᴇʏ,
 ᴛʜɪs ɪs {BOT_NAME} ,
ᴀɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴩ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ.*

ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ : [ᴛᴇʟᴇᴛʜᴏɴ](https://github.com/LonamiWebs/Telethon)
[ᴩʏʀᴏɢʀᴀᴍ](https://github.com/pyrogram/pyrogram)
[ᴩʏᴛʜᴏɴ-ᴛᴇʟᴇɢʀᴀᴍ-ʙᴏᴛ](https://github.com/python-telegram-bot/python-telegram-bot)
ᴀɴᴅ ᴜsɪɴɢ [sǫʟᴀʟᴄʜᴇᴍʏ](https://www.sqlalchemy.org) ᴀɴᴅ [ᴍᴏɴɢᴏ](https://cloud.mongodb.com) ᴀs ᴅᴀᴛᴀʙᴀsᴇ.

*ʜᴇʀᴇ ɪs ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ :* [{BOT_NAME}](https://github.com/bluefloyd24/helper)


𝗕𝗹𝘂𝗲 ʀᴏʙᴏᴛ ɪs ʟɪᴄᴇɴsᴇᴅ ᴜɴᴅᴇʀ ᴛʜᴇ [ᴍɪᴛ ʟɪᴄᴇɴsᴇ](https://github.com/bluefloyd24/helper/blob/master/LICENSE).
© 2024 [sᴜᴘᴘᴏʀᴛ](https://t.me/{SUPPORT_CHAT}) ᴄʜᴀᴛ, ᴀʟʟ ʀɪɢʜᴛs ʀᴇsᴇʀᴠᴇᴅ.
""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="👻", callback_data="start_back"),
                        InlineKeyboardButton(text="🚀️", callback_data="ABG_admin"),
                        InlineKeyboardButton(text="💵", callback_data="ABG_credit"),
                        InlineKeyboardButton(text="📎‍", url=f"tg://user?id={OWNER_ID}"),
                        InlineKeyboardButton(text="⬅️️", callback_data="help_back"),
                    ],
                    [
                        InlineKeyboardButton(
                            text="𝗦𝗼𝘂𝗿𝗰𝗲",
                            url="https://github.com/Bluefloyd24/helper",  # DON'T CHANGE
                        ),
                    ],
                ]
            ),
        )


about_callback_handler = CallbackQueryHandler(
    ABG_about_callback, pattern=r"ABG_", run_async=True
)

source_callback_handler = CallbackQueryHandler(
    Source_about_callback, pattern=r"source_", run_async=True
)

dispatcher.add_handler(about_callback_handler)
dispatcher.add_handler(source_callback_handler)
