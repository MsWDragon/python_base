import yaml
import os


def add_dir(config_file: str):
    '''Создает структуру папок на основе файла config.yaml'''
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    print(BASE_DIR)


    with open (f'{config_file}', 'r', encoding='utf-8') as fr:
        text_1 = yaml.safe_load(fr)
        for keys in text_1:
            dir_1 = os.path.join(BASE_DIR, keys)
            if not os.path.exists(dir_1):
                os.mkdir(dir_1)
        for values_1 in text_1[keys]:
            dir_2 = os.path.join(dir_1, values_1)
            if not os.path.exists(dir_2):
                os.mkdir(dir_2)

base_dir_1 = add_dir('config.yaml')