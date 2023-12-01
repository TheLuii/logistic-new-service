import logging


from keyboard import main_admin, main_manager, main_user, get_report_kb

from aiogram import types, F, Router
from aiogram.utils.markdown import hbold

admin_id = 453578228
manager_id = 4535782  #28
user_id = 45357822  #8


router = Router()


@router.callback_query(F.data == 'get_back_to_main')
async def get_back_to_main(c: types.CallbackQuery) -> None:
    logging.warning(f"Пользователь {c.from_user.full_name} {c.from_user.id} пытается перейти в главное меню")
    ID = c.from_user.id
    if ID == admin_id:
        await c.message.edit_text(f"{hbold('Главное меню')}",
                                  reply_markup=main_admin)
    elif ID == manager_id:
        await c.message.edit_text(f"{hbold('Главное меню')}",
                                  reply_markup=main_manager)
    elif ID == user_id:
        await c.message.edit_text(f"{hbold('Главное меню')}",
                                  reply_markup=main_user)
    else:
        await c.message.edit_text(f"Что то не так {ID} {c.from_user.full_name}")
        logging.error(f"User cannot get back to main menu\n{c.message}")



@router.callback_query(F.data == 'get_report')
async def get_reports(c: types.CallbackQuery) -> None:
    logging.warning(f"Пользователь {c.from_user.full_name} {c.from_user.id} выгрузил отчеты")
    await c.message.edit_text(f"Вот отчеты по направлениям", reply_markup=get_report_kb)