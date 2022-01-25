def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    # пишите реализацию своей программы здесь
    idx = 0
    while idx < len(list_in):
        el = list_in[idx]
        if str.isalpha(el):
            idx +=1
        elif str(el).startswith('+'):
            num = int(list_in[idx])
            list_in[idx] = '+{0:02d}'.format(num)
            list_in.insert(idx, '"')
            list_in.insert(idx + 2, '"')
            idx += 3
        elif str(el).startswith('-'):
            num = int(list_in[idx])
            list_in[idx] = '-{0:02d}'.format(num)
            list_in.insert(idx, '"')
            list_in.insert(idx + 2, '"')
            idx += 3
        else:
            num = int(list_in[idx])
            list_in[idx] = '{0:02d}'.format(num)
            list_in.insert(idx, '"')
            list_in.insert(idx + 2, '"')
            idx += 3
    str_out = ' '.join(list_in)
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(my_list))
result = convert_list_in_str(my_list)
print(my_list)
print(id(result))
print(result)
