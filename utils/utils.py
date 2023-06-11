# Функция для показа характеристик деталей или автомобилей
def show_values(dictionary: dict) -> str:
    result = ''
    for item in dictionary.keys():
        model = dictionary[item][0]
        count = dictionary[item][1]
        price = dictionary[item][2]
        result += f'Модель: {model}\
Количество на складе: {count}\
Цена: {price}\n\n'
    return result