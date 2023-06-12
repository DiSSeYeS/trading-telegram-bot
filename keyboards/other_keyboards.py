from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


# Создаем кнопки для выбора между покупкой машин и деталей
button_1: KeyboardButton = KeyboardButton(text='Машины')
button_2: KeyboardButton = KeyboardButton(text='Детали')

other_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2]],
                                               resize_keyboard=True,
                                               one_time_keyboard=True)

# Создаем кнопки "Да"-"Нет" создания для клавиатуры
button_yes: KeyboardButton = KeyboardButton(text='Да')
button_no: KeyboardButton = KeyboardButton(text='Нет')

simple_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_yes, button_no]],
                                               resize_keyboard=True,
                                               one_time_keyboard=True)

# Создаем кнопки с командами для создания клавиатуры
button_help: KeyboardButton = KeyboardButton(text='/help')
button_buy: KeyboardButton = KeyboardButton(text='/купить')
button_show_cart: KeyboardButton = KeyboardButton(text='/корзина')
button_clear_cart: KeyboardButton = KeyboardButton(text='/очистка')

commands_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_help, button_buy, button_show_cart, button_clear_cart]],
                                    resize_keyboard=True,
                                    one_time_keyboard=False)
