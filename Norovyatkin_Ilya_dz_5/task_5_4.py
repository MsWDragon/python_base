import numpy as np
import sys
from time import perf_counter


def get_numbers(src: list):
    for i in range(len(src)):
        if i > 0 and src[i] > src[i-1]:
            yield src[i]


# раскомментить для проверки на рандомных списках из 20 чисел от 0 до 100
src_1 = np.random.randint(0, 100, 30)
start = perf_counter()
print(src_1)
print(*get_numbers(src_1), '\n', perf_counter() - start)

start = perf_counter()
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src), '\n', perf_counter() - start)

''' С увеличением чисел в списке, скорость обработки через генератор падает, 
для оптимизации можно использовать обработку через цикл (код ниже \/), однако это использует больше памяти
поэтому в угоду памяти при больших списках используем генераторы, в угоду скорости обработки используем цикл и списки
'''


def get_numbers_adv(src_1: list):
    get_numbers_1 = []
    for i in range(len(src_1)):
        if i > 0 and src_1[i] > src_1[i-1]:
            get_numbers_1.append(src_1[i])
    return get_numbers_1


number_ = get_numbers_adv(src_1)
number_1 = get_numbers_adv(src)

start = perf_counter()
print(src_1)
print(number_1, '\n', perf_counter() - start, '\n', sys.getsizeof(number_))

start = perf_counter()
print(number_, '\n', perf_counter() - start, '\n', sys.getsizeof(number_1))


