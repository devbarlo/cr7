import os
from PIL import Image, ImageDraw, ImageFont
from . import *


def text_set(text):
    lines = []
    if len(text) <= 55:
        lines.append(text)
    else:
        all_lines = text.split("\n")
        for line in all_lines:
            if len(line) <= 55:
                lines.append(line)
            else:
                k = int(len(line) / 55)
                for z in range(1, k + 2):
                    lines.append(line[((z - 1) * 55) : (z * 55)])
    return lines[:25]
    

@Rallsthon.on(QQ070_cmd(pattern="رساله ?(.*)"))
async def writer(e):
    if e.reply_to:
        reply = await e.get_reply_message()
        text = reply.message
    elif e.pattern_match.group(1):
        text = e.text.split(maxsplit=1)[1]
    else:
        return await e.edit("**- بالـرد على نص او .رساله + النص**")
    img = Image.open("QQ070/malath/ppho.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("QQ070/malath/zarz.ttf", 30)
    x, y = 150, 140
    lines = text_set(text)
    line_height = font.getsize("hg")[1]
    for line in lines:
        draw.text((x, y), line, fill=(1, 22, 55), font=font)
        y = y + line_height - 5
    file = "QQ070.jpg"
    img.save(file)
    await e.reply(file=file)
    os.remove(file)
    await e.delete()
