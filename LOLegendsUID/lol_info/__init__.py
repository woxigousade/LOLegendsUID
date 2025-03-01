from gsuid_core.sv import SV
from gsuid_core.bot import Bot
from gsuid_core.models import Event
from gsuid_core.utils.database.api import get_uid

from ..utils.error_reply import UID_HINT
from ..utils.database.models import LOLBind
from .draw_lol_info_pic import draw_lol_info_img

lol_user_info = SV('LOL用户信息查询')


@lol_user_info.on_command(('查询'), block=True)
async def send_majs_search_msg(bot: Bot, ev: Event):
    uid = await get_uid(bot, ev, LOLBind)
    if uid is None:
        return await bot.send(UID_HINT)
    await bot.send(await draw_lol_info_img(ev, uid))
