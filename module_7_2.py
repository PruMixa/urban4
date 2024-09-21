def custom_write(file_name, strings):
    string_position = {}
    file = open(file_name, 'w', encoding='UTF-8')
    for i, string in enumerate(strings, 1):
        string_position[(i, file.tell())] = string
        file.write(string + '\n')
    file.close()
    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)