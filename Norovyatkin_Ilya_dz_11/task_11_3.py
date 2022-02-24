class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        # self.my_list = [int(i) for i in input('Введите значения через пробел ').split()]
        # val = int(input('Введите значения и нажимайте Enter - '))
        # self.my_list.append(val)
        while True:
                val = input('Введите значения и нажимайте Enter - ')
                if val == 'Stop' or val == 'stop':
                    return f'Текущий список - {self.my_list} \nВы вышли'
                else:
                    try:
                        val_1 = int(val)
                        self.my_list.append(val_1)
                        print(f'Текущий список - {self.my_list} \nдля выхода введите "Stop" \n')
                    except:
                        print(f"Недопустимое значение - строка и булево")
                        y_or_n = input(f'Попробовать еще раз? Y/N ')

                        if y_or_n == 'Y' or y_or_n == 'y':
                            None
                        elif y_or_n == 'N' or y_or_n == 'n':
                            return f'Вы вышли'
                        else:
                            return f'Вы вышли'
                
try_except = Error(1)
print(try_except.my_input())