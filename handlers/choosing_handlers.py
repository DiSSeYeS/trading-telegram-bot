from aiogram.types import Message
from aiogram import Router
from lexicon.ru_lexicon import LEXICON_RU
from states import USERS
from keyboards import vehicle_keyboard, details_keyboard
from filters import select_details_filter, select_vehicles_filter


# Инициализируем роутер уровня модуля
router: Router = Router()

# Хэндел для распознавания сообщения, текстом которого является "машины"
# и состояние пользователя которого нулевое
@router.message(select_vehicles_filter)
async def choose_vehicle(message: Message):
    if message.from_user is not None:
        USERS[message.from_user.id]['condition'] = 'in_process'

    await message.answer(text=LEXICON_RU['Машины'], reply_markup=vehicle_keyboard)

# Хэндел для распознавания сообщения, текстом которого является "детали"
# и состояние пользователя которого нулевое
@router.message(select_details_filter)
async def choose_detail(message: Message):
    if message.from_user is not None:
        USERS[message.from_user.id]['condition'] = 'in_process'

    await message.answer(text=LEXICON_RU['Детали'], reply_markup=details_keyboard)
