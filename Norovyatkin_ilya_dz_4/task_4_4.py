import utils
def main(argv):
    program, *args = argv
    x = " ".join(args)
    print(utils.currency_rates(x))

    return 0


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))


#Не вышло сделать нормальный многострочный коментарий, терминал начинает ругаться в конце 
#File "C:\Users\msw98\OneDrive\Рабочий стол\python_base\Norovyatkin_Ilya_dz_4\task_4_4.py", line 23
#    '''
#      ^
#SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 688-689: truncated \UXXXXXXXX escape
#
#
#
#PS C:\Users\msw98\OneDrive\Рабочий стол\python_base\Norovyatkin_Ilya_dz_4> python task_4_4.py USD
#76.4849
#PS C:\Users\msw98\OneDrive\Рабочий стол\python_base\Norovyatkin_Ilya_dz_4> python task_4_4.py kzt
#0.176253
#PS C:\Users\msw98\OneDrive\Рабочий стол\python_base\Norovyatkin_Ilya_dz_4> python task_4_4.py dKk
#11.6081    