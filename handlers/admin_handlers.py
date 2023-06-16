from aiogram import Router


# Инициализируем роутер уровня модуля
router: Router = Router()

#router.message.filter(lambda msg: USERS[msg.from_user.id]['status'] == 'admin' or msg.from_user.id in ADMINLIST)