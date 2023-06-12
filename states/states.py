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

# Получаем словарь со списокм деталей
# где их ID - это ключ, а значение - количество на складе и цена
DETAILS = {
    '000001' : ['Картюратор', '10', '999'],
    '000002' : ['Двигатель', '2', '4.999'],
    '000003' : ['Мотор', '0', '349'],
    '000004' : ['Глушитель', '12', '499']
}

# Получаем словарь со списокм автомобилей
# где их ID - это ключ, а значение - количество на складе и цена
VEHICLES = {
    '000001' : ['Tesla Model S 2022', '2', '249.900'],
    '000002' : ['Lada Vesta 2023', '4', '49.900'],
    '000003' : ['Жигули "Четёврка" 2002', '0', '99.000'],
    '000004' : ['Mercedes Benz 2019', '7', '149.900']
}

# Создаем список со значениями кнопок для деталей
DETAILS_BUTTONS_VALUES: list[str] = get_buttons_values(DETAILS)

# Создаем список со значениями кнопок для машин
VEHICLES_BUTTONS_VALUES: list[str] = get_buttons_values(VEHICLES)