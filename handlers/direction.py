import logging
from aiogram import Dispatcher, types, F, Router


from keyboard import manage_direction_menu

dp = Dispatcher()
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
router = Router()


@router.callback_query(F.data == 'manage_direction')
async def manage_direction_main_menu(c: types.CallbackQuery) -> None:
    logging.warning(f"Пользователь {c.from_user.full_name} {c.from_user.id} пытается перейти в меню с направлениями")
    await c.message.edit_text(f"Выбери нужный вариант", reply_markup=manage_direction_menu)


