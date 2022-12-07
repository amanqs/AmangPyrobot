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


@Ayiin(["gban", "gban"])
async def _(e):
    xx = await e.eor("`Gbanning...`")
    reason = ""
    if e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
        try:
            reason = e.text.split(" ", maxsplit=1)[1]
        except IndexError:
            pass
    elif e.pattern_match.group(1).strip():
        usr = e.text.split(maxsplit=2)[1]
        try:
            userid = await e.client.parse_id(usr)
        except ValueError:
            userid = usr
        try:
            reason = e.text.split(maxsplit=2)[2]
        except IndexError:
            pass
    elif e.is_private:
        userid = e.chat_id
        try:
            reason = e.text.split(" ", maxsplit=1)[1]
        except IndexError:
            pass
    else:
        return await xx.eor("`Reply to some msg or add their id.`", time=5)
    user = None
    try:
        user = await e.client.get_entity(userid)
        name = inline_mention(user)
    except BaseException:
        userid = int(userid)
        name = str(userid)
    chats = 0
    if userid == (await event.client.get_me()).id:
        return await xx.eor("`I can't gban myself.`", time=3)
    elif userid in DEVLIST:
        return await xx.eor("`I can't gban my Developers.`", time=3)
    elif is_gbanned(userid):
        return await eod(
            xx,
            "`User is already gbanned and added to gbanwatch.`",
            time=4,
        )
    if e.client._dialogs:
        dialog = e.client._dialogs
    else:
        dialog = await e.client.get_dialogs()
        e.client._dialogs.extend(dialog)
    for ggban in dialog:
        if ggban.is_group or ggban.is_channel:
            try:
                await e.client.edit_permissions(ggban.id, userid, view_messages=False)
                chats += 1
            except FloodWaitError as fw:
                LOGS.info(
                    f"[FLOOD_WAIT_ERROR] : on GBAN Command\nSleeping for {fw.seconds+10}"
                )
                await asyncio.sleep(fw.seconds + 10)
                try:
                    await e.client.edit_permissions(
                        ggban.id, userid, view_messages=False
                    )
                    chats += 1
                except BaseException as er:
                    LOGS.exception(er)
            except (ChatAdminRequiredError, ValueError):
                pass
            except BaseException as er:
                LOGS.exception(er)
    gban(userid, reason)
    if isinstance(user, User):
        await e.client(BlockRequest(userid))
    gb_msg = f"**#Gbanned** {name} `in {chats} chats and added to gbanwatch!`"
    if reason:
        gb_msg += f"\n**Reason** : {reason}"
    await xx.edit(gb_msg)
    
    CMD_HELP.update(
    {"gban": (
        "gban",
        {
            "gbantst <reply>": "Forward Broadcast messages in group chats.",
            "gtst <reply>": "Broadcast messages in group chats.",
            "gbncast <reply>": "Broadcast messages in user.",
        }
    )
    }
)
