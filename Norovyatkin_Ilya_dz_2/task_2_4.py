def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    # пишите реализацию своей программы здесь
    hello_list = []
    for name in list_in:
        name_parts = name.split(' ')
        name_1 = str.capitalize(name_parts.pop())
        hello_list.append(f'Привет, {name_1}!')
    list_out = hello_list
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(id(my_list))
result = convert_name_extract(my_list)
print(id(my_list))
print(result)