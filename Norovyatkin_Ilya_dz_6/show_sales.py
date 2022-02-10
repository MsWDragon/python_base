def show_sales(argv: str):
    '''Принимает аргументы и выводит данные из файла bakery.csv по принципу:\n
    без аргумета - выводит все записи \n
    с одним аргументом - выводить все записи с номера, равного этому числу, до конца\n
    с двумя аргументами - выводить записи, начиная с номера, равного первому числу, 
    по номер, равный второму числу, включительно'''

    
    with open('bakery.csv', 'r', encoding='utf-8') as fr:
        program, *args = argv
        content = fr.read()
        if len(args) == 0:
            print(content)
        elif len(args) == 1:
            x = '\n'.join(content.split('\n')[int(*args)-1:])
            print(x)
        elif len(args) == 2:
            y = '\n'.join(content.split('\n')[int(args[0])-1:int(args[1])])
            print(y)
    return 0


if __name__ == '__main__':
   import sys

   exit(show_sales(sys.argv))