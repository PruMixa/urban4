from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = '7809070886:AAG7LEYnKzkVEaRkBfjJgCGMoMvDkBLzcnM'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Главная клавиатура
keybut = ReplyKeyboardMarkup(resize_keyboard=True)
button_info = types.KeyboardButton(text='Информация')
button_calculate = types.KeyboardButton(text='Рассчитать')
button_buy = types.KeyboardButton(text='Купить')
keybut.add(button_info)
keybut.add(button_calculate)
keybut.add(button_buy)

# Inline-меню для расчета калорий
inboard = InlineKeyboardMarkup(row_width=2)
inbutt1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inbutt2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inboard.add(inbutt1, inbutt2)

# Inline-меню для покупки продуктов
inboard2 = InlineKeyboardMarkup(row_width=2)
inbutt3 = InlineKeyboardButton(text="Product1", callback_data="product_buying")
inbutt4 = InlineKeyboardButton(text="Product2", callback_data="product_buying")
inbutt5 = InlineKeyboardButton(text="Product3", callback_data="product_buying")
inbutt6 = InlineKeyboardButton(text="Product4", callback_data="product_buying")
inboard2.add(inbutt3, inbutt4, inbutt5, inbutt6)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! я бот помогающий твоему здоровью", reply_markup=keybut)


@dp.message_handler(text='Информация')
async def inform(message: types.Message):
    await message.answer("Бот для расчёта еды в рот")


@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer(text='Выберите опцию:', reply_markup=inboard)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer(text='10 х вес(кг) + 6,25 x рост(см) – 5 х возраст(г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
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
    await message.reply(f"Ваша норма калорий: {calories}")
    await state.finish()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(1, 5):
        await message.answer(f"Название: Product{i} | Описание: описание {i} | Цена: {i * 100}")
        with open(f'{i}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer("Выберите продукт для покупки:", reply_markup=inboard2)


@dp.callback_query_handler(text="product_buying")
async def end_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.message_handler()
async def all_message(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
