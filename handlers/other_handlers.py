from aiogram.types import Message
from aiogram import Router
from lexicon.ru_lexicon import LEXICON_RU
from states import USERS
from keyboards import commands_keyboard


# Инициализируем роутер уровня модуля
router: Router = Router()

# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме возможных команд
@router.message()
async def send_echo(message: Message):
    try:

        if message.from_user is not None and USERS[message.from_user.id]['condition'] in (None, 'menu'):
            await message.answer(text=LEXICON_RU['undefined_message'], reply_markup=commands_keyboard)

        elif message.from_user is not None and USERS[message.from_user.id]['condition'] == 'another_deleting_definition':
            USERS[message.from_user.id]['condition'] = 'menu'
            await message.answer(text=LEXICON_RU['gotcha'], reply_markup=commands_keyboard)

        else:
            if message.from_user is not None: USERS[message.from_user.id]['condition'] = 'menu'
            await message.answer(text=LEXICON_RU['undefined_message'], reply_markup=commands_keyboard)

    except TypeError:
        await message.reply(text=LEXICON_RU['error: Undefined Message_type'])