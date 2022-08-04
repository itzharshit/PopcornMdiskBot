from translation import *
from pyrogram import Client, filters
from plugins.groups import group_send_handler
from plugins.database import collection
from pymongo import TEXT
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)

@Client.on_message(filters.command('start'))
async def start_message(c,m):
    collection.create_index([("title" , TEXT),("caption", TEXT)],name="movie_index")
    if len(m.command) == 1:
        return await m.reply_photo("https://te.legra.ph/file/8b59ccda8500939d779c8.jpg",
            caption=START_MESSAGE.format(m.from_user.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Bot Dev", url='https://t.me/Akshay_Chand'),
                        InlineKeyboardButton("Our Group", url='https://t.me/iPapkornMovieGroup')
                    ]
                ]
            )
        )
    else:
        return await group_send_handler(c,m)

