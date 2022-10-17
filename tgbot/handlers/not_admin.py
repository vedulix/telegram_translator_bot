from aiogram import Dispatcher
from aiogram.types import Message


async def admin_start(message: Message):
    #await message.reply("Привет")
    ...

def register_not_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(admin_start, is_admin=True)
