# Task_1_2_a
def sum_list_1(dataset: list) -> int:
# создаю пустой список
    odd_number = []
# при помощи цикла и ветвления if из промежутка от 1 до 1000(включая 1000)
# отсеиваем все четные числа делением с остатком
# если остаток не равен 0, то это число возвести в 3 степень
    for number in dataset:
        if (number % 2 != 0):
            number **= 3
# добавить значение переменной number в список odd_number
            odd_number.append(number)
# проверял работоспособность данной части кода
#print(odd_number)

# вне циклов вводим переменные индекса int и конечной суммы чисел, 
# сумма цифр которых делится на 7 без остатка total_amount
    idx = 0 
    total_amount = 0
# цикл - пока значение idx меньше длины списка odd_number, выполнять следующее
    while idx < len(odd_number): 
# вводим переменную sum - в которой хранится значение суммы цифр
        sum = 0
# цикл - пока значение odd_number[idx] не равно 0, выполнять следующее
        while odd_number[idx] != 0:
# отбераем последнюю цифру путем деления с остатком на 10, и вписваем ее в переменную sum
            sum += odd_number[idx] % 10
# убераем последнюю цифру путем целочисленного деления на 10, полученное значение вписываем в odd_number[idx]
            odd_number[idx] //= 10
# делаем проверку, делится ли полученное число на 7 без остатка, если да, то прибавляем число из списка 
# к значению переменной total_amount
            if (sum % 7 == 0):
                total_amount += odd_number[idx]
# очередная проверка данной части кода)
    #odd_number[idx] = sum
# прибавляем к значению idx 1, для перехода к след числу в списке
        idx += 1
#print(odd_number)
# выводим конечный результат
    return(total_amount)
    print(total_amount)

#task_1_2_b
# тут все то же самое, за исключением того, что к каждому числу из промежутка прибавляем 17
def sum_list_2(dataset: list) -> int:
    odd_number = []
    for number in dataset:
        number += 17
        if (number % 2 != 0):
            number **= 3
            odd_number.append(number)
#print(odd_number)
    idx = 0 
    total_amount = 0
    while idx < len(odd_number): 
        sum = 0
        while odd_number[idx] != 0:
            sum += odd_number[idx] % 10
            odd_number[idx] //= 10
            if (sum % 7 == 0):
                total_amount += odd_number[idx]
    #odd_number[idx] = sum
        idx += 1
#print(odd_number)
    return(total_amount)
    print(total_amount)

my_list = []  # Соберите нужный список по заданию
for num_1 in range(1, 1001):
    my_list.append(num_1)

result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)