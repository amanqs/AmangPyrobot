# Ayiin - Ubot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/AyiinUbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/AyiinUbot/blob/main/LICENSE/>.
#
# FROM AyiinUbot <https://github.com/AyiinXd/AyiinUbot>
# t.me/AyiinChat & t.me/AyiinSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

from fipper import filters
from fipper.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from pyAyiin import __version__
from pyAyiin import tgbot
from pyAyiin.assistant import callback


START = """
👋🏻 Haii {}

🤖Nama saya{} 
🧑🏻‍💻Klik Tombol Dibawah Jika ingin membuat Userbot.
"""


@tgbot.on_message(filters.private & filters.incoming &
                  filters.command("start"))
async def start(bot, msg):
    user = await bot.get_me()
    mention = user.mention
    buttons = [
        [
            InlineKeyboardButton(
                "☞︎︎︎ Buat Userbot ☜︎︎︎", callback_data="multi_client")
        ],
        [
            InlineKeyboardButton(
                "Perintah", callback_data="help_or_command"), InlineKeyboardButton(
                "Tentang", callback_data="about")
        ],
    ]
    await bot.send_message(
        msg.chat.id,
        START.format(msg.from_user.mention, mention, __version__),
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@callback("help_or_command")
async def added_to_group_msg(client, cq):
    await cq.answer(
        "Sedang Tahap Percobaan...",
        show_alert=True,
    )


@callback("about")
async def added_to_group_msg(client, cq):
    await cq.answer(
        "Sedang Tahap Percobaan...",
        show_alert=True,
    )


@callback("multi_client")
async def added_to_group_msg(client, cq):
    await cq.message.reply(
        f"Silahkan Hubungi Admin Dibawah Ini",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("PM AMANG", callback_data="gen_string"),
                    InlineKeyboardButton("Kirim String", callback_data="sending_string"),
                ]
            ]
        )
    )


@callback("gen_string")
async def added_to_group_msg(_, cq):
    await cq.answer(
        "silahkan PC @amwang",
        show_alert=True,
    )


@callback("sending_string")
async def added_to_group_msg(_, cq):
    await cq.answer(
        "Modul Kirim String Belum Tersedia....",
        show_alert=True,
    )
