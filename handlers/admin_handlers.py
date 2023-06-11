from aiogram.types import Message
from aiogram import Router
from create_dp import dp
from lexicon.ru_lexicon import LEXICON_RU
from states import USERS, ADMINLIST


# Инициализируем роутер уровня модуля
router: Router = Router()

#router.message.filter(lambda msg: USERS[msg.from_user.id]['status'] == 'admin' or msg.from_user.id in ADMINLIST)