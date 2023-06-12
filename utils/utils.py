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

    values: list = []

    for item in dictionary.keys():
        count = dictionary[item][1]

        if count != 0:
            values.append(dictionary[item][0])

    return values

# Функция для получения списка с кнопками
def get_buttons(lst: list[str]) -> list[KeyboardButton]:

    buttons: list = []

    for iter in range(len(lst)):
        exec(f'button_{iter+1}: KeyboardButton = KeyboardButton(text=\'{lst[iter]}\')')
        buttons.append(eval(f'button_{iter+1}'))

    return buttons

# Функция для получения списка с кнопками при очистке корзины
def clear_cart_buttons(lst: list[str]) -> list[KeyboardButton]:

    buttons: list = []

    for iter in range(len(lst)):
        exec(f'cc_button_{iter+1}: KeyboardButton = KeyboardButton(text=\'{iter+1}\')')
        buttons.append(eval(f'cc_button_{iter+1}'))

    return buttons

# Функция для красивого отображения списка команд
def show_commands(dictionary: dict[str, str]) -> str:

    cmd_names = [item for item in dictionary.keys()]
    cmd_description = [item for item in dictionary.values()]

    result = ''

    for iter in range(len(cmd_names)):
        result += f'{iter+1}. {cmd_names[iter]} - {cmd_description[iter]}\n'

    return result

# Функция для определения ID товара по его названию
def id_definition(model: str, dictionary: dict[str, list]) -> str:

    for item in dictionary.keys():

        if model in dictionary[item]:
            return item

    return ' '

# Функция для отображения корзины
def show_cart(lst: list[str], dictionary: dict[str, list]) -> str:

    result: str = ''
    total_price: int = 0

    for iter in range(len(lst)):
        id = lst[iter]
        price = int(dictionary[id][2])
        total_price += price

        result += f'{iter+1}. {dictionary[id][0]} - {price} Р\n'

    result += f'\nОбщая цена - {total_price} Р'

    return result

# Функция для очистки корзины
def clear_cart(lst: list[str], index: int) -> list[str]:
    lst.pop(index)

    return lst
