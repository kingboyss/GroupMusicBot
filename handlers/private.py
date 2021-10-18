from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEMNJphbOXHgOFS0DzLRONLOVcSeBWpzAACWQADxUMaPYOO8zw7jO73IQQ")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://t.me/TheMp3Playebot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/TheMp3Playebot?startgroup=true"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/TheMp3Playebot?startgroup=true"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/TheMp3Playebot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/TheMp3Playebot")
                ]
            ]
        )
   )


