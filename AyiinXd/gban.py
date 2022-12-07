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

@Ayiin(["imp", "mweki"])
async def getbanned(ult):
    try:
        users = await ultroid_bot.get_participants(ult.chat_id,filter=banned)
    except Exception as e:
        return await eor(ult,f"ERROR - {str(e)}")
    if len(users) > 0 :
        msg=f"**LIST OF BANNED MEMBERS !!**\n\n=>> **TOTAL :** {len(users)}\n"
        for user in users:
            if not user.deleted:
                msg+=f"🛡[{user.first_name}]({user.id})\n"
            else:
                msg += "☠️ Deleted Account\n"
        await eor(ult,msg)
    else:
        await eor(ult,"No Banned Users !!")
