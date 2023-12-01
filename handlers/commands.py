import logging
'''
from keyboard import (main_admin,
                      main_manager,
                      main_user)
'''

import keyboard
from aiogram import  Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from db_func import get_user_role

'''
admin_id = 453578228
manager_id = 4535782  #28
user_id = 45357822  #8
'''

router = Router()

class RegForm(StatesGroup):
    get_new_name = State()
    get_phone_number = State()
    get_company_name = State()
    accept_data = State()





@router.message(CommandStart())
async def command_start_handler(message: Message,  state: FSMContext) -> None:
    ID = message.from_user.id
    user_role = get_user_role.get_user_role(ID)
    print(user_role)
    if  user_role == None:
        logging.warning(f"Пользователь {message.from_user.full_name} {message.from_user.id} инициализировал команду /start и начал регистрацию")
        await message.answer(f"Привет, давай зарегистрируемся в системе\n\nВведите ваше ФИО")
        await state.set_state(RegForm.get_new_name)
    elif user_role == 'admin':
        await message.answer(f"Привет, {hbold(message.from_user.full_name)}, ты Админ!",
                             reply_markup=keyboard.main_admin)
        logging.warning(f"Пользователь {message.from_user.full_name} {message.from_user.id} инициализировал команду /start")
    elif user_role == 'manager':
        await message.answer(f"Привет, {hbold(message.from_user.full_name)}, ты Менеджер!",
                             reply_markup=keyboard.main_manager)
        logging.warning(f"Пользователь {message.from_user.full_name} {message.from_user.id} инициализировал команду /start")
    elif user_role == 'user':
        await message.answer(f"Привет, {hbold(message.from_user.full_name)}, ты обычный Юзер!",
                             reply_markup=keyboard.main_user)
        logging.warning(f"Пользователь {message.from_user.full_name} {message.from_user.id} инициализировал команду /start")
    else:
        await message.answer(f"Error")


@router.message(RegForm.get_new_name)
async def get_phone_number(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(RegForm.get_phone_number)
    await message.answer(f"Отлично, теперь введи номер телефона по которому с тобой можно будет связаться")

@router.message(RegForm.get_phone_number)
async def get_company_name(message: Message, state: FSMContext) -> None:
    await state.update_data(phone_number=message.text)
    await state.set_state(RegForm.get_company_name)
    await message.answer(f"Теперь введи название компании")

@router.message(RegForm.get_company_name)
async def accept_info(message: Message, state: FSMContext):
    await state.update_data(company_name=message.text)
    await state.set_state(RegForm.accept_data)

@router.message(RegForm.accept_data)
async def accept_info_continue(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    name = data['name']
    phone_number = data['phone_number']
    company_name = data['company_name']
    print(name, phone_number, company_name)
    await message.answer(f"Давай проверим все ли верно\nТебя зовут {name}\nТвой номер телефона {phone_number}\nТы работаешь в компании {company_name}\nВсе верно?", reply_markup=keyboard.reg_user_kb)






