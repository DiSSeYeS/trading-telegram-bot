from config_data.config import Config, load_config
from utils import get_buttons_values


# Получаем словарь со списокм пользователей
# где их ID - это ключ, а значение - характеристики пользователя
USERS: dict = {}

# Загружаем конфиг в константу CONFIG
CONFIG: Config = load_config('.env')

# Загружаем токен бота в константу BOT_TOKEN
BOT_TOKEN: str = CONFIG.tg_bot.token

# Получаем ID суперадмина
SUPERADMIN: int = CONFIG.tg_bot.admin_ids[0]

# Получаем список ID админов
ADMINLIST: list[int] = CONFIG.tg_bot.admin_ids

# Получаем список с распознаваемыми боту командами
COMMANDS = ['/help', '/купить', '/корзина']

# Получаем словарь со списокм деталей
# где их ID - это ключ, а значение - количество на складе и цена
DETAILS = {
    '000001' : ['Карбюратор', '10', '999'],
    '000002' : ['Двигатель', '2', '4.999'],
    '000003' : ['Мотор', '0', '349'],
    '000004' : ['Глушитель', '12', '499']
}

# Получаем словарь со списокм автомобилей
# где их ID - это ключ, а значение - количество на складе и цена
VEHICLES = {
    '010001' : ['Tesla Model S 2022', '2', '249.900'],
    '010002' : ['Lada Vesta 2023', '4', '49.900'],
    '010003' : ['Жигули "Четёврка" 2002', '0', '99.000'],
    '010004' : ['Mercedes Benz 2019', '7', '149.900']
}

# Словарь со всеми товарами
ITEMS = {
    '000001' : ['Карбюратор', '10', '999'],
    '000002' : ['Двигатель', '2', '4999'],
    '000003' : ['Мотор', '0', '349'],
    '000004' : ['Глушитель', '12', '499'],
    '010001' : ['Tesla Model S 2022', '2', '249900'],
    '010002' : ['Lada Vesta 2023', '4', '49900'],
    '010003' : ['Жигули "Четёврка" 2002', '0', '99000'],
    '010004' : ['Mercedes Benz 2019', '7', '149900']
}

# Получаем список моделей автомобилей
VEHICLES_MODELS = [item[0] for item in VEHICLES.values()]

# Получаем список моделей деталей
DETAILS_MODELS = [item[0] for item in DETAILS.values()]

# Получаем список всех моделей
ALL_MODELS = VEHICLES_MODELS
ALL_MODELS.extend(DETAILS_MODELS)

# Создаем список со значениями кнопок для деталей
DETAILS_BUTTONS_VALUES: list[str] = get_buttons_values(DETAILS)

# Создаем список со значениями кнопок для машин
VEHICLES_BUTTONS_VALUES: list[str] = get_buttons_values(VEHICLES)

print(ALL_MODELS)
