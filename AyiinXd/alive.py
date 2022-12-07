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

import time

from fipper import Client, __version__ as fip_ver
from fipper.types import Message
from platform import python_version

from pyAyiin import __version__, ayiin_ver
from pyAyiin import CMD_HELP, HOSTED_ON, adB
from pyAyiin.decorator import Ayiin


from . import *


@Ayiin(["alive", "yins"])
async def aliveme(client: Client, message: Message):
    chat_id = message.chat.id
    user = await client.get_me()
    output = (
        f"**Tʜᴇ [AmangPyrobot](https://github.com/amanqs/AmangPyrobot)**\n\n"
        f"**ALIVE**\n\n"
        f"╭✠╼━━━━━━━━━━━━━━━✠╮\n"
        f"≽ **Bᴀsᴇ Oɴ :** •[{adB.name}]•\n"
        f"≽ **Oᴡɴᴇʀ :** [{user.first_name}](tg://user?id={user.id}) \n"
        f"≽ **Mᴏᴅᴜʟᴇs :** `{len(CMD_HELP)} Modules` \n"
        f"≽ **Pʏᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{python_version()}`\n"
        f"≽ **Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{fip_ver}`\n"
        f"≽ **Pʏ-Amang Vᴇʀsɪᴏɴ :** `{__version__}`\n"
        f"≽ **Bot Vᴇʀsɪᴏɴ :** `{ayiin_ver}` [{HOSTED_ON}]\n"
        "╰✠╼━━━━━━━━━━━━━━━✠╯\n\n"
    )


CMD_HELP.update(
    {"alive": (
        "alive",
        {
            "alive": "Check Your Userbot.",
        }
    )
    }
)
