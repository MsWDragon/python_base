def add_sale(argv):
    with open('bakery.csv', 'a', encoding='utf-8') as fa:
        program, *args = argv
        fa.write(f'{"".join(args)}\n')
    return 0


if __name__ == '__main__':
   import sys

   exit(add_sale(sys.argv))