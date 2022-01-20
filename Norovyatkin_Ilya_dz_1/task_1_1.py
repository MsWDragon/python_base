# Задаем несколько значений в виде списка
durations = [125869, 256873, 25000, 4000, 8563, 900, 53, 153, 4153, 400153]
# Используем цикл for для работоспособности кода для нескольких значений сразу
for duration in durations:
# Для конвертации значения в дни, используем оператор целочисленного деления (в 1 часу 3600 сек, в одном дне 24 часа)   
    days = duration // (24*3600)
# Для последующей работы, отделяем значение, превышающих колличество секунд в 1 сутках
# Используем оператор деления с остатком
    seconds = duration % (24 * 3600)
# Для получения значения снова используем оператор целочисленного деления (в 1 часу 3600 сек)
    hour = seconds // 3600
# Чтобы получить значение минут, я так же как и в случае с часами, сначала отделяю значение, первышающее колличество секунд в 1 часу
# (в 1 часу 3600 сек)
    seconds %= 3600
# Получаем колличество минут при помощи целочисленного деления (в 1 мин 60 сек)
    minutes = seconds // 60
# Используем деление с остатком и отделяем значение, превышающее колличесвто секунд в 1 минуте 
# Получаем колличество секунд (в 1 мин 60 сек)
    seconds %= 60
# Делаем проверку ветвлением для корректного вывода информации
# Если значение days больше 0, то выводим информацию в формате <d> дн <h> час <m> мин <s> сек
    if days > 0:
        print(f'{days} дн {hour} час {minutes} мин {seconds} сек')
# иначе продолжаем проверку
    else:
# Если значение hour больше 0, то выводим информацию в формате <h> час <m> мин <s> сек
        if hour > 0:
            print(f'{hour} час {minutes} мин {seconds} сек')
# иначе продолжаем проверку
        else:
# ЕСли значение minutes больше 0, то выводим информацию в формате <m> мин <s> сек
            if minutes > 0:
                print(f'{minutes} мин {seconds} сек')
# иначе выводим информацию в формате <s> сек
            else:
                print(f'{seconds} сек')
        
