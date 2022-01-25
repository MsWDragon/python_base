from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и 
        формирует из них единую строковую переменную разделяя значения запятой."""
    # пишите реализацию своей программы здесь
    str_inter = ''
    for n in list_in:
        r = int((n * 100) // 100)
        kk = int((n * 100) % 100)
        str_inter += str('{0} руб {1:02d} коп, '.format(r, kk))
    str_out = str_inter
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
print(id(my_list))
result_1 = transfer_list_in_str(my_list)
print(id(result_1))
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    # пишите реализацию здесь
    list_in.sort()
    list_out = list_in
    return list_out


# зафиксируйте здесь информацию по исходному списку my_list
print(my_list)
print(id(my_list))
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(id(result_2))
print(result_2)


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    my_list_1 = list.copy(my_list)
    my_list_1.sort(reverse=True)
    # пишите реализацию здесь
    list_out = my_list_1
    return list_out


result_3 = sort_price_adv(my_list)
print(id(my_list))
print(result_3)
print(id(result_3))

def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    # пишите реализацию здесь
    list_in.sort()
    list_out = list_in[:-6:-1]
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)