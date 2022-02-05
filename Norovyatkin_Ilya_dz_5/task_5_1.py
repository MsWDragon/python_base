def odd_nums(number: int) -> int:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
 # пишите свою реализацию здесь
    for num in range(1, number + 1, 2):
        yield num

n = 23
generator = odd_nums(n)
for _ in range(1, n+1, 2):
    print(next(generator))
next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration