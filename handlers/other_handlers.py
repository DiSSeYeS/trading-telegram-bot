from aiogram.types import Message
from aiogram import Router
from lexicon.ru_lexicon import LEXICON_RU
from states import USERS
from keyboards import commands_keyboard


# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@router.message()
async def send_echo(message: Message):

    try:
        await message.answer(text=LEXICON_RU['Сообщение не распознано'], reply_markup=commands_keyboard)

        if message.from_user is not None:
            USERS[message.from_user.id]['condition'] = None

    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])