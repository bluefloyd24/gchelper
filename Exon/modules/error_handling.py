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
import html
import io
import random
import sys
import traceback

import pretty_errors
import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext

from Exon import DEV_USERS
from Exon import LOG_GROUP_ID as ERROR_LOGS
from Exon import dispatcher
from Exon.modules.helper_funcs.decorators import Exoncmd

pretty_errors.mono()


class ErrorsDict(dict):
    """A custom dict to store errors and their count"""

    def __init__(self, *args, **kwargs):
        self.raw = []
        super().__init__(*args, **kwargs)

    def __contains__(self, error):
        self.raw.append(error)
        error.identifier = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=5))
        for e in self:
            if type(e) is type(error) and e.args == error.args:
                self[e] += 1
                return True
        self[error] = 0
        return False

    def __len__(self):
        return len(self.raw)


errors = ErrorsDict()


def error_callback(update: Update, context: CallbackContext):
    if not update:
        return

    if context.error not in errors:
        try:
            # Generate the pretty error message
            stringio = io.StringIO()
            pretty_errors.output_stderr = stringio
            pretty_errors.excepthook(
                type(context.error),
                context.error,
                context.error.__traceback__,
            )
            pretty_errors.output_stderr = sys.stderr
            pretty_error = stringio.getvalue()
            stringio.close()
        except Exception:
            pretty_error = "Failed to create pretty error."

        # Generate traceback
        tb_list = traceback.format_exception(
            None,
            context.error,
            context.error.__traceback__,
        )
        tb = "".join(tb_list)

        # Full error message
        pretty_message = (
            f'{pretty_error}\n-------------------------------------------------------------------------------\n'
            f'An exception was raised while handling an update\n'
            f'User: {update.effective_user.id}\n'
            f'Chat: {update.effective_chat.title if update.effective_chat else ""} '
            f'{update.effective_chat.id if update.effective_chat else ""}\n'
            f'Callback data: {update.callback_query.data if update.callback_query else "None"}\n'
            f'Message: {update.effective_message.text if update.effective_message else "No message"}\n\n'
            f'Full Traceback: {tb}'
        )

        # Send error message to external service
        extension = "txt"
        url = "https://spaceb.in/api/v1/documents/"
        try:
            response = requests.post(
                url, data={"content": pretty_message, "extension": extension}
            )
        except Exception as e:
            # Handle request failure
            print(f"Failed to send error log: {str(e)}")
            context.bot.send_message(
                ERROR_LOGS,
                text=f"Error log upload failed: {str(e)}",
                parse_mode="HTML",
            )
            return

        # Handle response from external service
        try:
            response_data = response.json()  # Attempt to parse JSON
        except requests.JSONDecodeError:
            print(f"Invalid JSON Response: {response.text}")  # Log non-JSON response
            response_data = None

        if response_data:
            url = f"https://spaceb.in/{response_data['payload']['id']}"
        else:
            url = None

        e = html.escape(f"{context.error}")
        if not url:
            # Fallback: Save to local file if external upload fails
            with open("error.txt", "w+") as f:
                f.write(pretty_message)
            context.bot.send_document(
                ERROR_LOGS,
                open("error.txt", "rb"),
                caption=f"#{context.error.identifier}\n<b>Your bot encountered an error:</b>\n<code>{e}</code>",
                parse_mode="HTML",
            )
            return

        # Send error message to error log group
        context.bot.send_message(
            ERROR_LOGS,
            text=f"#{context.error.identifier}\n<b>Your bot encountered an error:</b>\n<code>{e}</code>",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("View Error Logs", url=url)]],
            ),
            parse_mode="HTML",
        )
        else:
    print("Response is empty.")  # Handle empty response
    response_data = None


        url = f"https://spaceb.in/{response['payload']['id']}"
        context.bot.send_message(
            ERROR_LOGS,
            text=f"#{context.error.identifier}\n<b>Your Cute Exon Nagisa Have An Error For You:"
                 f"</b>\n<code>{e}</code>",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("sᴇxʏ ᴇxᴏɴ ᴇʀʀᴏʀ ʟᴏɢs", url=url)]],
            ),
            parse_mode=ParseMode.HTML,
        )


@Exoncmd(command="errors")
def list_errors(update: Update, context: CallbackContext):
    if update.effective_user.id not in DEV_USERS:
        return
    e = dict(sorted(errors.items(), key=lambda item: item[1], reverse=True))
    msg = "<b>Errors List:</b>\n"
    for x, value in e.items():
        msg += f"× <code>{x}:</code> <b>{value}</b> #{x.identifier}\n"
    msg += f"{len(errors)} have occurred since startup."
    if len(msg) > 4096:
        with open("errors_msg.txt", "w+") as f:
            f.write(msg)
        context.bot.send_document(
            update.effective_chat.id,
            open("errors_msg.txt", "rb"),
            caption="Too many errors have occured..",
            parse_mode="html",
        )
        return
    update.effective_message.reply_text(msg, parse_mode="html")


dispatcher.add_error_handler(error_callback)
