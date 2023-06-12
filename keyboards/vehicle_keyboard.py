from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from states import VEHICLES_BUTTONS_VALUES
from utils import get_buttons


# Создаем список с кнопками для выбора машины
buttons: list[KeyboardButton] = get_buttons(VEHICLES_BUTTONS_VALUES)

# Создаем клавиатуру с кнопками
vehicle_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[buttons],
                                               resize_keyboard=True,
                                               one_time_keyboard=True)