from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message


from tgbot.locals.load_json import data



async def start(message: Message, state: FSMContext):
    await message.answer(data.start.hi.text)


def register_start(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"], state="*")
