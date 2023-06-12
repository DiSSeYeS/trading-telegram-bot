from aiogram.types import Message
from aiogram import Router
from lexicon.ru_lexicon import LEXICON_RU
from states import USERS


# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@router.message()
async def send_echo(message: Message):

    try:
        await message.send_copy(chat_id=message.chat.id)

    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])