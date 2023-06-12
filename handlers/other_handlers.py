from aiogram.types import Message
from aiogram import Router
from create_dp import dp
from lexicon.ru_lexicon import LEXICON_RU
from states import USERS
from keyboards import vehicle_keyboard, details_keyboard


# Инициализируем роутер уровня модуля
router: Router = Router()

@router.message(lambda msg: USERS[msg.from_user.id]['condition'] == None and msg.text.lower() == 'машины')
async def choose_vehicle(message: Message):

    if message.from_user is not None:
        USERS[message.from_user.id]['condition'] = 'in_process'

    await message.answer(text=LEXICON_RU['Машины'], reply_markup=vehicle_keyboard)

    # Эту строчку надо будет убрать, она сделана для тестовых работ
    USERS[message.from_user.id]['condition'] = None

@router.message(lambda msg: USERS[msg.from_user.id]['condition'] == None and msg.text.lower() == 'детали')
async def choose_detail(message: Message):

    if message.from_user is not None:
        USERS[message.from_user.id]['condition'] = 'in_process'

    await message.answer(text=LEXICON_RU['Детали'], reply_markup=details_keyboard)

    # Эту строчку надо будет убрать, она сделана для тестовых работ
    USERS[message.from_user.id]['condition'] = None

# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@router.message()
async def send_echo(message: Message):

    try:
        await message.send_copy(chat_id=message.chat.id)

    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])