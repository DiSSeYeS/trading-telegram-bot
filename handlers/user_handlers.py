from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router
from create_dp import dp
from lexicon.ru_lexicon import LEXICON_RU
from states import USERS
from keyboards import other_keyboard

# Инициализируем роутер уровня модуля
router: Router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(lambda msg: msg.text == '/start')
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=other_keyboard)

    if message.from_user is not None and message.from_user.id not in USERS.keys():
        USERS[message.from_user.id] = {
            'username' : message.from_user.username,
            'status' : 'user',
            'condition' : None
        }

    #print(message.json(indent=4))
    #print(USERS.items())

# Этот хэндлер срабатывает на команду /help
@router.message(lambda msg: msg.text == '/help')
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])