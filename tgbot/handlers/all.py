from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from googletrans import Translator
import re


def is_russian(text):
  return bool(re.search('[\u0400-\u04FF]', text))

async def all(message: types.Message, state: FSMContext):
  text = message.text
  translator = Translator()

  if not is_russian(text):
    translated_text = f"<i>{translator.translate(text, src='en', dest='ru').text}</i>"
    await message.reply(translated_text)



def register_all(dp: Dispatcher):
  dp.register_message_handler(all, state="*")
