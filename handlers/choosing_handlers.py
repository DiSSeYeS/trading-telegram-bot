from aiogram.types import Message
from aiogram import Router
from lexicon.ru_lexicon import LEXICON_RU
from states import USERS, VEHICLES, DETAILS, ITEMS
from utils import id_definition, clear_cart
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

    await message.answer(text=LEXICON_RU['Машины'], reply_markup=vehicle_keyboard)

# Хэндел для распознавания сообщения, текстом которого является "детали"
# и состояние пользователя которого нулевое
@router.message(select_details_filter)
async def choose_detail(message: Message):
    if message.from_user is not None:
        USERS[message.from_user.id]['condition'] = 'choosing'

    await message.answer(text=LEXICON_RU['Детали'], reply_markup=details_keyboard)

# Хэндлер для уточнения, хочет ли человек добавить товар в корзину
@router.message(question_for_add_filter)
async def question_for_add_to_cart(message: Message):
    item = str(message.text)

    item_id = id_definition(item, ITEMS)

    if message.from_user is not None:
        USERS[message.from_user.id]['condition'] = 'adding_to_cart'
        USERS[message.from_user.id]['predict_cart'] = item_id

    await message.answer(text=f"{LEXICON_RU['Добавить в корзину']} {message.text}?", reply_markup=simple_keyboard)
    print(item_id)

# Хэндлер для распознавания согласия или отказа на добавления товара
@router.message(add_to_cart_filter)
async def add_to_cart(message: Message):
    text = str(message.text).lower()

    if text in ('да', 'добавить') and message.from_user is not None:
        USERS[message.from_user.id]['cart'].append(USERS[message.from_user.id]['predict_cart'])
        USERS[message.from_user.id]['predict_cart'] = []
        USERS[message.from_user.id]['condition'] = 'undefined'
        await message.answer(text=LEXICON_RU['Товар добавлен'], reply_markup=simple_keyboard)
        print(USERS[message.from_user.id]['cart'])

    else:
        if message.from_user is not None:
            await message.answer(text=LEXICON_RU['Товар не добавлен'], reply_markup=simple_keyboard)
            USERS[message.from_user.id]['condition'] = 'undefined'

# Хэндлер для обработки пользователя в неопределенном состоянии
# после согласия или отказа на добавление в корзину
@router.message(definition_filter)
async def definition_of_condition(message: Message):
    text = str(message.text).lower()

    if text == 'да' and message.from_user is not None:
        USERS[message.from_user.id]['condition'] = None
        await message.answer(text=LEXICON_RU['Соглашение'], reply_markup=other_keyboard)

    else:
        if message.from_user is not None: USERS[message.from_user.id]['condition'] = None
        await message.answer(text=LEXICON_RU['Отказ'], reply_markup=commands_keyboard)

# Хэндлер для обработки пользователя в состоянии очистки корзины
@router.message(cleaning_cart_filter)
async def definition_of_deleting(message: Message):
    try:
        index: int = int(message.text) - 1
        if message.from_user is not None and index in range(len(USERS[message.from_user.id]['cart'])):
            user_cart: list[str] = USERS[message.from_user.id]['cart']
            item_to_delete: str = ITEMS[user_cart[index]][0]
            await message.answer(text=f'Вы хотите удалить из корзины {item_to_delete}, верно?',
                                                                                reply_markup=simple_keyboard)
            USERS[message.from_user.id]['condition'] = 'deleting_item'
            USERS[message.from_user.id]['item_to_delete'] = index
        else:
            await message.answer(text='Думаю, в вашей корзине нет столько позиций :(', reply_markup=commands_keyboard)
            if message.from_user is not None: USERS[message.from_user.id]['condition'] = None
    except:
        await message.answer(text='Кажется, я не смог понять, какая позиция вам нужна :(', reply_markup=commands_keyboard)
        if message.from_user is not None: USERS[message.from_user.id]['condition'] = None

# Хэндлер для обработки пользователя в состоянии удаления позиции из корзины
@router.message(deleting_item_filter)
async def cart_deleting_item(message: Message):
    text = str(message.text).lower()

    if text == 'да' and message.from_user is not None:
        user_cart: list[str] = USERS[message.from_user.id]['cart']
        index = USERS[message.from_user.id]['item_to_delete']
        USERS[message.from_user.id]['cart'] = clear_cart(user_cart, index)
        USERS[message.from_user.id]['condition'] = 'another_deleting_definition'
        await message.answer(text='Позиция успешно удалена!\n\nЖелаете удалить из корзины что-то еще?', reply_markup=simple_keyboard)

    elif text == 'нет' and message.from_user is not None:
        USERS[message.from_user.id]['condition'] = None
        await message.answer(text='Понял вас!', reply_markup=commands_keyboard)