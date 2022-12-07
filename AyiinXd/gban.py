# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-UserBot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-UserBot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from fipper import Client, enums
from fipper.errors import FloodWait
from fipper.types import Message

from pyAyiin import Ayiin, CMD_HELP, DEVS
from pyAyiin.pyrogram import eor

from . import yins


@Ayiin(["fgcast"])
async def gban_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        AyiinXD = await message.reply("`Gbanning...`")
    else:
        AyiinXD = await message.edit("`Gbanning....`")
    if not user_id:
        return await AyiinXD.edit("Saya tidak dapat menemukan pengguna itu.")
    if user_id == client.me.id:
        return await AyiinXD.edit("**Ngapain NgeGban diri sendiri Goblok 🐽**")
    if user_id in DEVS:
        return await AyiinXD.edit("**Gagal GBAN karena dia adalah Pembuat saya 🗿**")
    if user_id in WHITELIST:
        return await AyiinXD.edit(
            "**Gagal GBAN karena dia adalah admin @SharingUserbot 🗿**"
        )
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await AyiinXD.edit("`Harap tentukan pengguna yang valid!`")

    if sql.is_gbanned(user.id):
        return await AyiinXD.edit(
            f"[Jamet](tg://user?id={user.id}) **ini sudah ada di daftar gbanned**"
        )
    f_chats = await get_ub_chats(client)
    if not f_chats:
        return await AyiinXD.edit("**Anda tidak mempunyai GC yang anda admin 🥺**")
    er = 0
    done = 0
    for gokid in f_chats:
        try:
            await client.ban_chat_member(chat_id=gokid, user_id=int(user.id))
            done += 1
        except BaseException:
            er += 1
    sql.gban(user.id)
    msg = (
        r"**\\#GBanned_User//**"
        f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    msg += f"\n**Affected To:** `{done}` **Chats**"
    await AyiinXD.edit(msg)
    
    
    )
    
    
    CMD_HELP.update(
    {"gban": (
        "gban",
        {
            "fgcast <reply>": "Forward Broadcast messages in group chats.",
            "gcast <reply>": "Broadcast messages in group chats.",
            "gucast <reply>": "Broadcast messages in user.",
        }
    )
    }
)
