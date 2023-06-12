from states import ADMINLIST, USERS


__all__ = ('admin_filter', 'start_command_filter', 'help_command_filter',
           'select_vehicles_filter', 'select_details_filter')

# Фильтер для распознавания хэндлерами админов
admin_filter = lambda msg: msg.from_user.id in ADMINLIST

# Фильтер для распознавания хэндлерами сообщений 'машины' от людей в состоянии None
select_vehicles_filter = lambda msg: USERS[msg.from_user.id]['condition'] == None and msg.text.lower() == 'машины'

# Фильтер для распознавания хэндлерами сообщений 'детали' от людей в состоянии None
select_details_filter = lambda msg: USERS[msg.from_user.id]['condition'] == None and msg.text.lower() == 'детали'

# Фильтер для распознавания хэндлерами комманды "/start"
start_command_filter = lambda msg: msg.text == '/start'

# Фильтер для распознавания хэндлерами комманды "/help"
help_command_filter = lambda msg: msg.text == '/help'
