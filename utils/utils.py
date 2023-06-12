from aiogram.types import KeyboardButton


# Функция для показа характеристик деталей или автомобилей
def show_values(dictionary: dict) -> str:

    result = ''

    for item in dictionary.keys():
        model = dictionary[item][0]
        count = dictionary[item][1]
        price = dictionary[item][2]

        if int(count) != 0:
            result += f'Модель: {model}\n\
Количество на складе: {count}\n\
Цена: {price}\n\n'

    return result

# Функция для получения типа деталей/названия автомобиля
# для установки его в кнопки
def get_buttons_values(dictionary: dict) -> list[str]:

    values = []

    for item in dictionary.keys():
        count = dictionary[item][1]

        if count != 0:
            values.append(dictionary[item][0])

    return values

# Функция для получения количества кнопок
def get_buttons(lst: list[str]) -> list[KeyboardButton]:

    buttons = []

    for i in range(len(lst)):
        exec(f'button_{i+1}: KeyboardButton = KeyboardButton(text=\'{lst[i]}\')')
        buttons.append(eval(f'button_{i+1}'))

    return buttons