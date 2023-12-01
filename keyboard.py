from aiogram.types import (InlineKeyboardMarkup,
                           InlineKeyboardButton)



reg_user_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да, все верно', callback_data='yes_register')
        ],
        [
            InlineKeyboardButton(text='Нет, заполнить данные заного', callback_data='no_rest_reg_and_go_again')
        ]
    ]
)

main_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Управление пользователями', callback_data='manage_users')
        ],
        [
            InlineKeyboardButton(text='Управление направлениями', callback_data='manage_direction')
        ],
        [
            InlineKeyboardButton(text='Отчеты', callback_data='get_report')
        ],
        [
            InlineKeyboardButton(text='Мой профиль', callback_data='my_profile')
        ]
    ]
)

main_manager = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Управление пользователями', callback_data='manage_users')
        ],
        [
            InlineKeyboardButton(text='Управление направлениями', callback_data='manage_direction')
        ],
        [
            InlineKeyboardButton(text='Мой профиль', callback_data='my_profile')
        ]
    ]
)

main_user = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Мой профиль', callback_data='my_profile')
        ],
        [
            InlineKeyboardButton(text='Доступные направления', callback_data='open_direction')
        ],
        [
            InlineKeyboardButton(text='Мои направления', callback_data='my_direction')
        ]
    ]
)

my_profile = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Изменить данные', callback_data='change_user_info')
        ],
        [
            InlineKeyboardButton(text='Вернуться в главное меню', callback_data='get_back_to_main')
        ]
    ]
)

manage_users = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Вывести список поставщиков', callback_data='get_all_users')
        ],
        [
            InlineKeyboardButton(text='Вывести список менеджеров', callback_data='get_only_manages')
        ],
        [
            InlineKeyboardButton(text='Вернуться в главное меню', callback_data='get_back_to_main')
        ]
    ]
)

manage_users_get_suppliers = InlineKeyboardMarkup(
    inline_keyboard=[
       [
           InlineKeyboardButton(text='Вернуться назад', callback_data='manage_users')
       ]
    ]
)

manage_users_get_managers = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Вернуться назад', callback_data='manage_users')
        ]
    ]
)

manage_direction_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Открыть новое направление', callback_data='open_new_direction')
        ],
        [
            InlineKeyboardButton(text='Показать список открытых направлений', callback_data='get_all_open_direction_list')
        ],
        [
            InlineKeyboardButton(text='Вернуться в главное меню', callback_data='get_back_to_main')
        ]
    ]
)

change_user_info = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Изменить ФИО', callback_data='change_username')
        ],
        [
            InlineKeyboardButton(text='Изменить название компании', callback_data='change_user_company')
        ],
        [
            InlineKeyboardButton(text='Изменить номер телефона', callback_data='change_user_phone')
        ],
        [
            InlineKeyboardButton(text='Вернуться назад', callback_data='my_profile')
        ]
    ]
)

get_report_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Вернуться в главное меню', callback_data='get_back_to_main')
        ]
    ]
)