def transform_string(number: int) -> str:
# делаем проверку, если деление с остатком значения переменной percent на 100 больше или равно 10 и меньше либо равно 20,
# (тоесть под это условие попадают значения от 10 до 20), то выводим значение и слово 'процентов'
    if number % 100 >= 10 and number % 100 <= 20:
        print(f'{number} процентов')
# иначе, если деление с остатком значения переменной percent на 10 равно 1
# (по это условие попадают значения 1, 21, 31, 41, 51, 61, 71, 81, 91)
# то выводим значение и слово 'процент'
    elif number % 10 == 1:
        print(f'{number} процент')
# если деление с остатком значения переменной percent на 10 больше или равно 2 и меньше либо равно 4,
# (тоесть под это условие попадают значения от 2 до 4, от 22 до 24, от 32 до 34 ... от 92 до 94), 
# то выводим значение и слово 'процента'
    elif number % 10 >= 2 and number % 10 <= 4:
        print(f'{number} процента')
# если значение переменной не подошло ни под одно из выше указанных условий,
# то выводим значение и слово процентов
    else:
        print(f'{number} процентов')
    return()
# создаем цикл для перебора значений  промежутке от 1 до 100 (включая 100)
for n in range (1, 101):
    print(transform_string(n))
