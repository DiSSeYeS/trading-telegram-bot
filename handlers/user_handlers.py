from aiogram.types import Message
from aiogram import Router
from lexicon.ru_lexicon import LEXICON_RU
from states import USERS, ITEMS
from utils import show_cart
from keyboards import other_keyboard, commands_keyboard
from filters import (start_command_filter, help_command_filter,
                    buying_filter, show_cart_filter, clear_cart_filter)
from aiogram.types import ReplyKeyboardMarkup
from utils import clear_cart_buttons


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
            'condition' : None,
            'cart' : [],
            'predict_cart' : []
        }
        print(USERS[message.from_user.id])

# Этот хэндлер срабатывает на команду /help
@router.message(help_command_filter)
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])

# Этот хэндлер срабатыват на команду /купить
@router.message(buying_filter)
async def process_buying_command(message: Message):
    await message.answer(text=LEXICON_RU['Радость'], reply_markup=other_keyboard)

    if message.from_user is not None:
        USERS[message.from_user.id]['condition'] = None

# Этот хэндлер срабатывает на команду /корзина
@router.message(show_cart_filter)
async def process_show_cart_command(message: Message):
    if message.from_user is not None and USERS[message.from_user.id]['cart'] != []:
        await message.answer(text=show_cart(USERS[message.from_user.id]['cart'], ITEMS))

    else:
        await message.answer(text='Ваша корзина пуста\n\nЗаполним её? :)', reply_markup=commands_keyboard)

# Этот хэндлер срабатывает на команду /очистка
@router.message(clear_cart_filter)
async def process_clear_cart_command(message: Message):

    if message.from_user is not None:

        # Создаем клавиатуру с кнопками, соответствующими позициям в корзине
        cc_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                        keyboard=[clear_cart_buttons(USERS[message.from_user.id]['cart'])],
                                        resize_keyboard=True,
                                        one_time_keyboard=False)

        cart_info = show_cart(USERS[message.from_user.id]['cart'], ITEMS)
        if USERS[message.from_user.id]['cart'] != []:
            USERS[message.from_user.id]['condition'] = 'cleaning_cart'
            await message.answer(text=f'Какой товар Вы желаете удалить?\n\n{cart_info}', reply_markup=cc_keyboard)
        else:
            await message.answer(text='Вам нечего удалять, корзина пуста\n\n', reply_markup=commands_keyboard)