def show_sales(argv):
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