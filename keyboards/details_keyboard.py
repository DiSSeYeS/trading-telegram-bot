from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)


# Создаем кнопки для взаимодействия с деталями
button_1: KeyboardButton = KeyboardButton(text='Деталь 1')
button_2: KeyboardButton = KeyboardButton(text='Деталь 2')
button_3: KeyboardButton = KeyboardButton(text='Деталь 3')
button_4: KeyboardButton = KeyboardButton(text='Деталь 4')

# Создаем клавиатуру с кнопками
details_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2,
                                               button_3, button_4]],
                                               resize_keyboard=True,
                                               one_time_keyboard=True)