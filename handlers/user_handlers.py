from aiogram.types import Message
from aiogram import Router
from lexicon.ru_lexicon import LEXICON_RU
from states import USERS
from keyboards import other_keyboard
from filters import start_command_filter, help_command_filter

# Инициализируем роутер уровня модуля
router: Router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(start_command_filter)
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=other_keyboard)

    if message.from_user is not None and message.from_user.id not in USERS.keys():
        USERS[message.from_user.id] = {
            'username' : message.from_user.username,
            'status' : 'user',
            'condition' : None
        }

# Этот хэндлер срабатывает на команду /help
@router.message(help_command_filter)
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])