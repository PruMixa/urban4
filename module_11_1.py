from PIL import Image

# открываем фото
image = Image.open('image.jpg')

# изменяем размер
resized_image = image.resize((256, 256))

# применяем эффект сепия
sepia_image = resized_image.convert('L')
sepia_image = sepia_image.point(lambda p: p * (1 - 0.6) + 130)

# сохранение в другом формате
sepia_image.save('my_image.png')

import numpy as np

array = np.array([1, 2, 3, 4, 5])

sum_array = np.sum(array)  # сумма элементов
mean_array = np.mean(array)  # среднее значение
std_array = np.std(array)  # стандартное отклонение

print("Массив:", array)
print("Сумма:", sum_array)
print("Среднее значение:", mean_array)
print("Стандартное отклонение:", std_array)

import pandas as pd

data = pd.read_csv('data.csv')

print("Первые 5 строк:")
print(data.head())

print("\nИнформация о данных:")
print(data.info())

print("\nСтатистические характеристики:")
print(data.describe())

print("\nСортировка по колонке 'Age':")
print(data.sort_values(by='Age'))
