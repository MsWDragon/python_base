import os
import shutil
from pprint import pprint


def collecting_templates(format: str, folder: str):
    '''
    Собирает файлы в указанную папку
    :param format: - формат файлов которые нужно собрать
    :param folder: - название папки в которую нужно собрать
    '''

    # определяем путь, отностильно которого будем работать
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # задаем путь до папки с проектом
    project_dir = os.path.join(BASE_DIR, 'my_project_1')
    '''с помощью рекурсивного обхода папок, находим папки с шаблонами
    при помощи цикла разделяем список на dir - путь и dir_1 - список папок''' 
    for dir, *dir_1 in os.walk(project_dir):
        # ищем в списке папок находим нужную нам
        if ['templates'] in dir_1:
            # задаем путь до нее
            temp_dir = os.path.join(dir, 'templates')
            # формируем список вложений
            list_1 = os.listdir(temp_dir)
            # формируем список вложений в родительсикх папках
            list_2 = os.listdir(os.path.join(temp_dir, *list_1))
            # перебераем вложения
            for filename in list_2:
                # находим файлы с нужным нам форматом
                if filename.endswith(format):
                    # формируем путь до файла
                    file_dir = os.path.join(temp_dir, *list_1, filename)
                    # формируем путь до папки в которую нужно все поместить
                    folder_dir = os.path.join(project_dir, folder, *list_1)
                    # проеряем нет ли уже такой папки
                    if not os.path.exists(folder_dir):
                        # создаем папку
                        os.makedirs(folder_dir)
                    # копируем файлы с нужным расширением в нужную папку
                    shutil.copy2(file_dir, folder_dir)
            
            
collecting_templates('html', 'templates')