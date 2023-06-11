from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)


# Создаем кнопки для выбора между покупкой машин и деталей
button_1: KeyboardButton = KeyboardButton(text='Машины')
button_2: KeyboardButton = KeyboardButton(text='Детали')

other_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2,]],
                                               resize_keyboard=True,
                                               one_time_keyboard=True)