from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards import button_cancel
from states import DETAILS_BUTTONS_VALUES
from utils import get_buttons


# Создаем список с кнопками для выбора типа детали
buttons: list[KeyboardButton] = get_buttons(DETAILS_BUTTONS_VALUES)

# Создаем клавиатуру с кнопками
details_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[buttons, [button_cancel]],
                                               resize_keyboard=True,
                                               one_time_keyboard=True)