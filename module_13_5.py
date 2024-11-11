from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = '7809070886:AAG7LEYnKzkVEaRkBfjJgCGMoMvDkBLzcnM'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

keybut = ReplyKeyboardMarkup()
button1 = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Расчитат')
keybut.add(button1)
keybut.add(button2)
keybut = types.ReplyKeyboardMarkup(resize_keyboard=True)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer("Бот для расчёта еды в рот")


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! я бот помогающий твоему здоровью", reply_markup=keybut)


@dp.message_handler(text='Расчитат')
async def set_age(message: types.Message, state: FSMContext):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    calories = (10 * weight) + (6.25 * growth) - (5 * age) + 5
    await message.reply(f"Ваша норма калорий {calories}")
    await state.finish()


@dp.message_handler()
async def all_message(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
