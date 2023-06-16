from aiogram.types import Message
from aiogram import Router
from lexicon.ru_lexicon import LEXICON_RU
from states import USERS, ITEMS, VEHICLES, DETAILS
from utils import id_definition, clear_cart, show_values
from keyboards import (vehicle_keyboard, details_keyboard, simple_keyboard,
                        other_keyboard, commands_keyboard)
from filters import (select_details_filter, select_vehicles_filter,
                        question_for_add_filter, add_to_cart_filter,
                        definition_filter, cleaning_cart_filter, deleting_item_filter)


# Инициализируем роутер уровня модуля
router: Router = Router()

# Хэндел для распознавания сообщения, текстом которого является "машины"
# и состояние пользователя которого нулевое
@router.message(select_vehicles_filter)
async def choose_vehicle(message: Message):
    if message.from_user is not None:
        USERS[message.from_user.id]['condition'] = 'choosing'

    if message.from_user is not None: print(USERS[message.from_user.id]['condition'], message.from_user.id)
    await message.answer(text=f'{LEXICON_RU["vehicles_pt1"]}{show_values(VEHICLES)}\
{LEXICON_RU["vehicles_pt2"]}', reply_markup=vehicle_keyboard)


# Хэндел для распознавания сообщения, текстом которого является "детали"
# и состояние пользователя которого нулевое
@router.message(select_details_filter)
async def choose_detail(message: Message):
    if message.from_user is not None:
        USERS[message.from_user.id]['condition'] = 'choosing'

    if message.from_user is not None: print(USERS[message.from_user.id]['condition'], message.from_user.id)
    await message.answer(text=f'{LEXICON_RU["details_pt1"]}{show_values(DETAILS)}\
{LEXICON_RU["details_pt2"]}', reply_markup=details_keyboard)


# Хэндлер для уточнения, хочет ли человек добавить товар в корзину
@router.message(question_for_add_filter)
async def question_for_add_to_cart(message: Message):
    item = str(message.text)

    item_id = id_definition(item, ITEMS)

    if message.from_user is not None:
        USERS[message.from_user.id]['condition'] = 'adding_to_cart'
        USERS[message.from_user.id]['predict_cart'] = item_id

    if message.from_user is not None: print(USERS[message.from_user.id]['condition'], message.from_user.id)
    if message.from_user is not None: print(item_id, message.from_user.id)
    await message.answer(text=f"{LEXICON_RU['add_to_cart']} {message.text}?", reply_markup=simple_keyboard)


# Хэндлер для распознавания согласия или отказа на добавления товара
@router.message(add_to_cart_filter)
async def add_to_cart(message: Message):
    text = str(message.text).lower()

    if text in (LEXICON_RU['yes'], LEXICON_RU['add']) and message.from_user is not None:
        USERS[message.from_user.id]['cart'].append(USERS[message.from_user.id]['predict_cart'])
        USERS[message.from_user.id]['predict_cart'] = []
        USERS[message.from_user.id]['condition'] = 'undefined'
        await message.answer(text=LEXICON_RU['added_to_cart'], reply_markup=simple_keyboard)
        print(USERS[message.from_user.id]['cart'])

    else:
        if message.from_user is not None:
            USERS[message.from_user.id]['condition'] = 'undefined'
            await message.answer(text=LEXICON_RU['not_added_to_cart'], reply_markup=simple_keyboard)
    if message.from_user is not None: print(USERS[message.from_user.id]['condition'], message.from_user.id)


# Хэндлер для обработки пользователя в неопределенном состоянии
# после согласия или отказа на добавление в корзину
@router.message(definition_filter)
async def definition_of_condition(message: Message):
    text = str(message.text).lower()

    if text == LEXICON_RU['yes'] and message.from_user is not None:
        USERS[message.from_user.id]['condition'] = None
        await message.answer(text=LEXICON_RU['agree'], reply_markup=other_keyboard)

    else:
        if message.from_user is not None: USERS[message.from_user.id]['condition'] = 'menu'
        await message.answer(text=LEXICON_RU['deny'], reply_markup=commands_keyboard)
    if message.from_user is not None: print(USERS[message.from_user.id]['condition'], message.from_user.id)


# Хэндлер для обработки пользователя в состоянии очистки корзины
@router.message(cleaning_cart_filter)
async def definition_of_deleting(message: Message):
    try:
        index: int = int(str(message.text)) - 1
        if message.from_user is not None and index in range(len(USERS[message.from_user.id]['cart'])):
            user_cart: list[str] = USERS[message.from_user.id]['cart']
            item_to_delete: str = ITEMS[user_cart[index]][0]
            await message.answer(text=f'{LEXICON_RU["specify_part1"]}{item_to_delete}{LEXICON_RU["specify_part2"]}',
                                                                                reply_markup=simple_keyboard)
            USERS[message.from_user.id]['condition'] = 'deleting_item'
            USERS[message.from_user.id]['item_to_delete'] = index

        else:
            await message.answer(text=LEXICON_RU['too_much_positions'], reply_markup=commands_keyboard)
            if message.from_user is not None: USERS[message.from_user.id]['condition'] = 'menu'

    except:
        if message.from_user is not None: USERS[message.from_user.id]['condition'] = 'menu'
        await message.answer(text=LEXICON_RU['undefined_position'], reply_markup=commands_keyboard)

    if message.from_user is not None: print(USERS[message.from_user.id]['condition'], message.from_user.id)


# Хэндлер для обработки пользователя в состоянии удаления позиции из корзины
@router.message(deleting_item_filter)
async def cart_deleting_item(message: Message):
    text = str(message.text).lower()

    if text == LEXICON_RU['yes'] and message.from_user is not None:
        user_cart: list[str] = USERS[message.from_user.id]['cart']
        index = USERS[message.from_user.id]['item_to_delete']

        if len(USERS[message.from_user.id]['cart']) != 1:
            USERS[message.from_user.id]['condition'] = 'another_deleting_definition'
            USERS[message.from_user.id]['cart'] = clear_cart(user_cart, index)
            await message.answer(text=LEXICON_RU['position_cleaned_with_continue'], reply_markup=simple_keyboard)

        else:
            USERS[message.from_user.id]['condition'] = 'menu'
            USERS[message.from_user.id]['cart'] = clear_cart(user_cart, index)
            await message.answer(text=LEXICON_RU['position_cleaned_without_continue'], reply_markup=commands_keyboard)

    elif text == LEXICON_RU['no'] and message.from_user is not None:
        USERS[message.from_user.id]['condition'] = 'menu'
        await message.answer(text=LEXICON_RU['gotcha'], reply_markup=commands_keyboard)

    else:
        if message.from_user is not None: USERS[message.from_user.id]['condition'] = 'menu'
        await message.answer(text=LEXICON_RU['undefined_message'], reply_markup=commands_keyboard)

    if message.from_user is not None: print(USERS[message.from_user.id]['condition'], message.from_user.id)
