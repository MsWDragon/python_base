import os


def file_size(folder: str) -> dict:
    '''
    выводит статистику для заданной папки в виде словаря, 
    в котором ключи — верхняя граница размера файла (пусть будет кратна 10), 
    а значения — общее количество файлов (в том числе и в подпапках), 
    размер которых не превышает этой границы, но больше предыдущей (начинаем с 0)
    '''
    before_100 = 0
    before_1000 = 0
    before_10000 = 0
    before_100000 = 0
    more_100000 = 0
    for root, dirs, files in os.walk(folder):
        if len(files) > 0:
            for item in os.scandir(root):
                if os.DirEntry.is_file(item):
                    if item.stat().st_size < 100:
                        before_100 += 1
                    elif item.stat().st_size < 1000:
                        before_1000 += 1
                    elif item.stat().st_size < 10000:
                        before_10000 += 1
                    elif item.stat().st_size < 100000:
                        before_100000 += 1
                    else:
                        more_100000 += 1
                    #print(root, len(files), item.stat().st_size)
    if more_100000 > 0:
        dict_size = {100:before_100, 1000:before_1000, 10000:before_10000, 100000:before_100000, 'more':more_100000}
    elif before_100000 > 0:
        dict_size = {100:before_100, 1000:before_1000, 10000:before_10000, 100000:before_100000}
    elif before_10000 > 0:
        dict_size = {100:before_100, 1000:before_1000, 10000:before_10000}
    elif before_1000 > 0:
        dict_size = {100:before_100, 1000:before_1000}
    else:
        dict_size = {100:before_100}
    return dict_size


_dir = os.path.dirname(os.path.abspath(__file__))
print(file_size(_dir)) # {100: 22, 1000: 2, 10000: 2}