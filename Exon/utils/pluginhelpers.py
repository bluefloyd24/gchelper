"""
MIT License

Copyright (c) 2022 ABIAHNOI69 

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

import asyncio
import math
import shlex
import sys
import time
import traceback
from functools import wraps
from typing import Callable, Coroutine, Dict, List, Tuple, Union

import aiohttp
from PIL import Image
from pyrogram import Client
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Chat, Message, User

from Exon import OWNER_ID, SUPPORT_CHAT, Abishnoi
from Exon.utils.errors import split_limits


def get_user(message: Message, text: str) -> [int, str, None]:
    asplit = None if text is None else text.split(" ", 1)
    user_s = None
    reason_ = None
    if message.reply_to_message:
        user_s = message.reply_to_message.from_user.id
        reason_ = text or None
    elif asplit is None:
        return None, None
    elif len(asplit[0]) > 0:
        user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        if len(asplit) == 2:
            reason_ = asplit[1]
    return user_s, reason_


async def is_admin(event, user):
    try:
        sed = await event.client.get_permissions(event.chat_id, user)
        is_mod = bool(sed.is_admin)
    except Exception:
        is_mod = False
    return is_mod


def get_readable_time(seconds: int) -> int:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += f"{time_list.pop()}, "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
            (f"{str(days)} day(s), " if days else "")
            + (f"{str(hours)} hour(s), " if hours else "")
            + (f"{str(minutes)} minute(s), " if minutes else "")
            + (f"{str(seconds)} second(s), " if seconds else "")
            + (f"{str(milliseconds)} millisecond(s), " if milliseconds else "")
    )
    return tmp[:-2]


async def delete_or_pass(message):
    if message.from_user.id == 1141839926:
        return message
    return await message.delete()


def humanbytes(size):
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return f"{str(round(size, 2))} {dict_power_n[raised_to_pow]}B"


async def progress(current, total, message, start, type_of_ps, file_name=None):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        if elapsed_time == 0:
            return
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join("🔴" for _ in range(math.floor(percentage / 10))),
            "".join("🔘" for _ in range(10 - math.floor(percentage / 10))),
            round(percentage, 2),
        )

        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            try:
                await message.edit(f"{type_of_ps}\n**File Name:** `{file_name}`\n{tmp}")
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass
        else:
            try:
                await message.edit(f"{type_of_ps}\n{tmp}")
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass


def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " not in text_to_return:
        return None

    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        return None


async def iter_chats(client):
    chats = []
    async for dialog in client.iter_dialogs():
        if dialog.chat.type in ["supergroup", "channel"]:
            chats.append(dialog.chat.id)
    return chats


async def fetch_audio(client, message):
    time.time()
    if not message.reply_to_message:
        await message.reply("`Reply To A Video / Audio.`")
        return
    warner_stark = message.reply_to_message
    if warner_stark.audio is None and warner_stark.video is None:
        await message.reply("`Format Not Supported`")
        return
    if warner_stark.video:
        lel = await message.reply("`Video Detected, Converting To Audio !`")
        warner_bros = await message.reply_to_message.download()
        stark_cmd = f"ffmpeg -i {warner_bros} -map 0:a friday.mp3"
        await runcmd(stark_cmd)
        final_warner = "friday.mp3"
    elif warner_stark.audio:
        lel = await edit_or_reply(message, "`Download Started !`")
        final_warner = await message.reply_to_message.download()
    await lel.edit("`Almost Done!`")
    await lel.delete()
    return final_warner


async def edit_or_reply(message, text, parse_mode="md"):
    if message.from_user.id:
        if message.reply_to_message:
            kk = message.reply_to_message.message_id
            return await message.reply_text(
                text, reply_to_message_id=kk, parse_mode=parse_mode
            )
        return await message.reply_text(text, parse_mode=parse_mode)
    return await message.edit(text, parse_mode=parse_mode)


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    """run command in terminal"""
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


async def convert_to_image(message, client) -> [None, str]:
    """Convert Most Media Formats To Raw Image"""
    final_path = None
    if not (
            message.reply_to_message.photo
            or message.reply_to_message.sticker
            or message.reply_to_message.media
            or message.reply_to_message.animation
            or message.reply_to_message.audio
    ):
        return None
    if message.reply_to_message.photo:
        final_path = await message.reply_to_message.download()
    elif message.reply_to_message.sticker:
        if message.reply_to_message.sticker.mime_type == "image/webp":
            final_path = "webp_to_png_s_proton.png"
            path_s = await message.reply_to_message.download()
            im = Image.open(path_s)
            im.save(final_path, "PNG")
        else:
            path_s = await client.download_media(message.reply_to_message)
            final_path = "lottie_proton.png"
            cmd = (
                f"lottie_convert.py --frame 0 -if lottie -of png {path_s} {final_path}"
            )
            await runcmd(cmd)
    elif message.reply_to_message.audio:
        thumb = message.reply_to_message.audio.thumbs[0].file_id
        final_path = await client.download_media(thumb)
    elif message.reply_to_message.video or message.reply_to_message.animation:
        final_path = "fetched_thumb.png"
        vid_path = await client.download_media(message.reply_to_message)
        await runcmd(f"ffmpeg -i {vid_path} -filter:v scale=500:500 -an {final_path}")
    return final_path


def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " not in text_to_return:
        return None

    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        return None


# Admin check

admins: Dict[str, List[User]] = {}


def get(chat_id: Union[str, int]) -> Union[List[User], bool]:
    if isinstance(chat_id, int):
        chat_id = str(chat_id)

    return admins[chat_id] if chat_id in admins else False


async def get_administrators(chat: Chat) -> List[User]:
    if _get := get(chat.id):
        return _get
    set(
        chat.id,
        (member.user for member in await chat.get_member(filter="administrators")),
    )

    return await get_administrators(chat)


def admins_only(func: Callable) -> Coroutine:
    async def wrapper(client: Client, message: Message):
        if message.from_user.id == OWNER_ID:
            return await func(client, message)
        admins = await get_administrators(message.chat)
        for admin in admins:
            if admin.id == message.from_user.id:
                return await func(client, message)

    return wrapper


# @Mr_Dark_Prince
def capture_err(func):
    @wraps(func)
    async def capture(client, message, *args, **kwargs):
        try:
            return await func(client, message, *args, **kwargs)
        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errors = traceback.format_exception(
                etype=exc_type,
                value=exc_obj,
                tb=exc_tb,
            )
            error_feedback = split_limits(
                "**ERROR** | `{}` | `{}`\n\n```{}```\n\n```{}```\n".format(
                    message.from_user.id if message.from_user else 0,
                    message.chat.id if message.chat else 0,
                    message.text or message.caption,
                    "".join(errors),
                ),
            )
            for x in error_feedback:
                await Abishnoi.send_message(SUPPORT_CHAT, x)
            raise err

    return capture


# Special credits to TheHamkerCat


async def member_permissions(chat_id, user_id):
    perms = []
    member = await Abishnoi.get_chat_member(chat_id, user_id)
    if member.can_post_messages:
        perms.append("can_post_messages")
    if member.can_edit_messages:
        perms.append("can_edit_messages")
    if member.can_delete_messages:
        perms.append("can_delete_messages")
    if member.can_restrict_members:
        perms.append("can_restrict_members")
    if member.can_promote_members:
        perms.append("can_promote_members")
    if member.can_change_info:
        perms.append("can_change_info")
    if member.can_invite_users:
        perms.append("can_invite_users")
    if member.can_pin_messages:
        perms.append("can_pin_messages")
    return perms


async def current_chat_permissions(chat_id):
    perms = []
    perm = (await Abishnoi.get_chat(chat_id)).permissions
    if perm.can_send_messages:
        perms.append("can_send_messages")
    if perm.can_send_media_messages:
        perms.append("can_send_media_messages")
    if perm.can_send_stickers:
        perms.append("can_send_stickers")
    if perm.can_send_animations:
        perms.append("can_send_animations")
    if perm.can_send_games:
        perms.append("can_send_games")
    if perm.can_use_inline_bots:
        perms.append("can_use_inline_bots")
    if perm.can_add_web_page_previews:
        perms.append("can_add_web_page_previews")
    if perm.can_send_polls:
        perms.append("can_send_polls")
    if perm.can_change_info:
        perms.append("can_change_info")
    if perm.can_invite_users:
        perms.append("can_invite_users")
    if perm.can_pin_messages:
        perms.append("can_pin_messages")

    return perms


# URL LOCK


def get_url(message_1: Message) -> Union[str, None]:
    messages = [message_1]

    if message_1.reply_to_message:
        messages.append(message_1.reply_to_message)

    text = ""
    offset = None
    length = None

    for message in messages:
        if offset:
            break

        if message.entities:
            for entity in message.entities:
                if entity.type == "url":
                    text = message.text or message.caption
                    offset, length = entity.offset, entity.length
                    break

    return None if offset in (None,) else text[offset: offset + length]


async def fetch(url):
    async with aiohttp.ClientSession() as session, session.get(url) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def convert_seconds_to_minutes(seconds: int):
    seconds = seconds
    seconds %= 24 * 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


async def json_object_prettify(objecc):
    dicc = objecc.__dict__
    return "".join(
        f"**{key}:** `{value}`\n"
        for key, value in dicc.items()
        if key not in ["pinned_message", "photo", "_", "_client"]
    )


async def json_prettify(data):
    output = ""
    try:
        for key, value in data.items():
            output += f"**{key}:** `{value}`\n"
    except Exception:
        for datas in data:
            for key, value in datas.items():
                output += f"**{key}:** `{value}`\n"
            output += "------------------------\n"
    return output
