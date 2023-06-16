from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


# Создаем универсальную кнопку отмены
button_cancel: KeyboardButton = KeyboardButton(text='/cancel')

# Создаем кнопки для выбора между покупкой машин и деталей
button_1: KeyboardButton = KeyboardButton(text='Машины')
button_2: KeyboardButton = KeyboardButton(text='Детали')

other_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2], [button_cancel]],
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
button_buy: KeyboardButton = KeyboardButton(text='/buy')
button_show_cart: KeyboardButton = KeyboardButton(text='/cart')
button_clear_cart: KeyboardButton = KeyboardButton(text='/clear_cart')

commands_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_help, button_buy, button_show_cart, button_clear_cart]],
                                    resize_keyboard=True,
                                    one_time_keyboard=False)
