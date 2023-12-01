import logging
from aiogram import types, F, Router

from keyboard import (manage_users,
                      manage_users_get_managers,
                      manage_users_get_suppliers)




logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
router = Router()



@router.callback_query(F.data == 'manage_users')
async def manage_users_main(c: types.CallbackQuery) -> None:
    logging.warning(f"Пользователь {c.from_user.full_name} {c.from_user.id} пытается перейти в меню управления пользователями")
    await c.message.edit_text(f"Выберите нужный вариант", reply_markupkeyboard=manage_users)

@router.callback_query(F.data == 'get_all_users')
async def manage_users_get_users(c: types.CallbackQuery) -> None:
    logging.warning(f"Пользователь {c.from_user.full_name} {c.from_user.id} пытается получить сисок всех пользователей")
    await c.message.edit_text(f"Тут будет список всех поставщиков", reply_markup=manage_users_get_suppliers)

@router.callback_query(F.data == 'get_only_manages')
async def manage_users_get_users(c: types.CallbackQuery) -> None:
    logging.warning(f"Пользователь {c.from_user.full_name} {c.from_user.id} пытается получить сисок всех менеджеров")
    await c.message.edit_text(f"Тут будет список всех менеджеров", reply_markup=manage_users_get_managers)