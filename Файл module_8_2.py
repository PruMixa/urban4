def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
    return result, incorrect_data


def calculate_average(numbers):
    try:
        if isinstance(numbers, (list, tuple, set)):
            sum_numbers, _ = personal_sum(numbers)
            return sum_numbers / len(numbers) if len(numbers) > 0 else 0
        else:
            print('В numbers записан некорректный тип данных')
            return None
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# Тестирование
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
