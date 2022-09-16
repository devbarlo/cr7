"""
©Ralls : @RallsThon
  - Ralls UpTime
  - Commend: .المده
"""

import time

from . import ALIVE_NAME, StartTime, get_readable_time, mention, reply_id

DEFULTUSER = ALIVE_NAME or "Rallsbot"
Ralls_IMG = "https://telegra.ph/file/57d51af1ca93d8cc8a958.jpg"
Ralls_TEXT = "𓆩 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑺𝑶𝑼𝑹𝑪𝑬 𝐑𝐀𝐈𝐈𝐒𝙏𝙃𝙊𝙉 𓆪"
RallsEM = "**⌔∮**"


@bot.on(admin_cmd(outgoing=True, pattern="المده$"))
@bot.on(sudo_cmd(pattern="المده$", allow_sudo=True))
async def uptRalls(Ralls):
    if Ralls.fwd_from:
        return
    Rallsid = await reply_id(Ralls)
    Rallsupt = await get_readable_time((time.time() - StartTime))
    if Ralls_IMG:
        Ralls_c = f"**{Ralls_TEXT}**\n"
        Ralls_c += f"**{RallsEM} المستخدم :** {mention}\n"
        Ralls_c += f"**{RallsEM} مدة التشغيل :** `{Rallsupt}`"
        await Ralls.client.send_file(Ralls.chat_id, Ralls_IMG, caption=Ralls_c, reply_to=Rallsid)
        await Ralls.delete()
    else:
        await edit_or_reply(
            Ralls,
            f"**{Ralls_TEXT}**\n\n"
            f"**{RallsEM} المستخدم :** {mention}\n"
            f"**{RallsEM} مدة التشغيل :** `{Rallsupt}`",
        )
