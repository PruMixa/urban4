from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

keybut = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = InlineKeyboardButton(text='Информация')
button2 = KeyboardButton(text='Расcчитать')
keybut.add(button1)
keybut.add(button2)

inboard = InlineKeyboardMarkup()
inbutt1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inbutt2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inboard.add(inbutt1)
inboard.add(inbutt2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Расcчитать')
async def main_menu(message):
    await message.answer(text='выберите опцию:', reply_markup=inboard)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(text='10 х вес(кг) + 6,25 x рост(см) – 5 х возраст(г) + 5')
    await call.answer()


@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer("Бот для расчёта еды в рот")


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст')
    await UserState.age.set()
    await call.answer()


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


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! я бот помогающий твоему здоровью", reply_markup=keybut)


@dp.message_handler()
async def all_message(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
