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


@Ayiin(["gban"])
async def gban(event):
    if event.fwd_from:
        return
    sender = await event.get_sender()
    me = await event.client.get_me()
    if sender.id != me.id:
        gbun = await event.reply(get_string("gban_2"))
    else:
        gbun = await edit_or_reply(event, get_string("gban_2"))
    start = datetime.now()
    user, reason = await get_user_from_event(event, gbun)
    if not user:
        return
    if user.id == (await event.client.get_me()).id:
        await gbun.edit("**𝙉𝙜𝙖𝙥𝙖𝙞𝙣 𝙉𝙜𝙚𝙂𝙗𝙖𝙣 𝘿𝙞𝙧𝙞 𝙎𝙚𝙣𝙙𝙞𝙧𝙞 𝙂𝙤𝙗𝙡𝙤𝙠 🐽**")
        return
    if user.id in DEVS:
        await gbun.edit(get_string("gban_5"))
        return
    if user.id in WHITELIST:
        await gbun.edit(get_string("gban_6"))
        return
    if gban_sql.is_gbanned(user.id):
        await gbun.edit(
            f"**𝙎𝙞** [𝙅𝙖𝙢𝙚𝙩](tg://user?id={user.id}) **𝙄𝙣𝙞 𝙎𝙪𝙙𝙖𝙝 𝘼𝙙𝙖 𝘿𝙞 𝘿𝙖𝙛𝙩𝙖𝙧 𝙂𝘽𝙖𝙣𝙣𝙚𝙙**"
        )
    else:
        gban_sql.freakgban(user.id, reason)
    san = []
    san = await admin_groups(event)
    count = 0
    fiz = len(san)
    if fiz == 0:
        await gbun.edit("**𝘼𝙣𝙙𝙖 𝙏𝙞𝙙𝙖𝙠 𝙈𝙚𝙢𝙥𝙪𝙣𝙮𝙖𝙞 𝙂𝙘 𝙔𝙖𝙣𝙜 𝘼𝙣𝙙𝙖 𝘼𝙙𝙢𝙞𝙣 🥺**")
        return
    await gbun.edit(
        f"**𝙄𝙣𝙞𝙩𝙞𝙖𝙩𝙞𝙣𝙜 𝙂𝙗𝙖𝙣 𝙊𝙛 𝙏𝙝𝙚** [𝙅𝙖𝙢𝙚𝙩](tg://user?id={user.id}) **𝙄𝙣** `{len(san)}` **𝙂𝙧𝙤𝙪𝙥𝙨**"
    )
    for i in range(fiz):
        try:
            await event.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**𝘼𝙣𝙙𝙖 𝙏𝙞𝙙𝙖𝙠 𝙈𝙚𝙢𝙞𝙡𝙞𝙠𝙞 𝙄𝙯𝙞𝙣 𝘽𝙖𝙣𝙣𝙚𝙙 𝘿𝙞 :**\n**𝙂𝙧𝙤𝙪𝙥 𝘾𝙝𝙖𝙩 :** `{event.chat_id}`",
            )
    end = datetime.now()
    timetaken = (end - start).seconds
    if reason:
        await gbun.edit(
            f"**\\#𝙂𝘽𝙖𝙣𝙣𝙚𝙙_𝙐𝙨𝙚𝙧//**\n\n**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚 :** [{user.first_name}](tg://user?id={user.id})\n**𝙐𝙨𝙚𝙧 𝙄𝘿 :** `{user.id}`\n**𝘼𝙘𝙩𝙞𝙤𝙣 : 𝙂𝘽𝙖𝙣𝙣𝙚𝙙 𝙄𝙣 {count} 𝙂𝙧𝙤𝙪𝙥𝙨**\n**𝘿𝙪𝙧𝙖𝙩𝙞𝙤𝙣 𝙂𝙗𝙖𝙣𝙣𝙚𝙙 :** `{timetaken}` **𝙎𝙚𝙘𝙤𝙣𝙙𝙨**!!\n**𝙍𝙚𝙖𝙨𝙤𝙣 :** `{reason}`\n**𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 : ✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧**"
        )
    else:
        await gbun.edit(
            f"**\\#𝙂𝘽𝙖𝙣𝙣𝙚𝙙_𝙐𝙨𝙚𝙧//**\n\n**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚 :** [{user.first_name}](tg://user?id={user.id})\n**𝙐𝙨𝙚𝙧 𝙄𝘿 :** `{user.id}`\n**𝘼𝙘𝙩𝙞𝙤𝙣 : 𝙂𝘽𝙖𝙣𝙣𝙚𝙙 𝙄𝙣 {count} 𝙂𝙧𝙤𝙪𝙥𝙨**\n**𝘿𝙪𝙧𝙖𝙩𝙞𝙤𝙣 𝙂𝙗𝙖𝙣𝙣𝙚𝙙 :** `{timetaken}` **𝙎𝙚𝙘𝙤𝙣𝙙𝙨**!!\n**𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 : ✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧**"
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
