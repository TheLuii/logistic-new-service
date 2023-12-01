import logging
from aiogram import Dispatcher, types, F, Router
import keyboard

router = Dispatcher()
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
router = Router()

@router.callback_query(F.data == 'my_profile')
async def my_profile(c: types.CallbackQuery) -> None:
    await c.message.edit_text('Вот ваш профиль', reply_markup=keyboard.my_profile)

@router.callback_query(F.data == 'change_user_info')
async def list_user_data_for_change(c: types.CallbackQuery) -> None:
    logging.warning(f"Пользователь {c.from_user.full_name} {c.from_user.id} пытается изменить свои данные")
    await c.message.edit_text(f"Что вы хотели бы изменить?", reply_markup=keyboard.change_user_info)

@router.callback_query(F.data == 'change_username')
async def change_username(c: types.CallbackQuery) -> None:
    await c.message.edit_text(f"В данный момент эта функция недоступна, нажми /start что бы вернуться в главное меню")

@router.callback_query(F.data == 'change_user_company')
async def change_user_company(c: types.CallbackQuery) -> None:
    await c.message.edit_text(f"В данный момент эта функция недоступна, нажми /start что бы вернуться в главное меню")

@router.callback_query(F.data == 'change_user_phone')
async def change_user_phone(c: types.CallbackQuery) -> None:
    await c.message.edit_text(f"В данный момент эта функция недоступна, нажми /start что бы вернуться в главное меню")