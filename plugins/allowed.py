from pyrogram import Client, filters
from pyrogram.types import Message
from info import PRIVATE_BOT, OWNER
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def owner(_, client, message: Message):
    if PRIVATE_BOT:
        return message.from_user.id != OWNER

allowed_user = filters.create(owner)

@Client.on_message(filters.private & allowed_user & filters.incoming)
async def not_owner(bot, message):
    btn = [[
        InlineKeyboardButton('Repo', url='https://t.me/MOVIE_WORLD_IN_MOVIE')
    ],[
        InlineKeyboardButton('Developer', url='https://t.me/kishan484')
    ]]
    await message.reply("You can't access this bot, Create your own bot.", reply_markup=InlineKeyboardMarkup(btn))
