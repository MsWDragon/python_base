import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """

    with open(f'{path_users_file}', 'r', encoding='utf-8') as fr1, open(f'{path_hobby_file}', 'r', encoding='utf-8') as fr2:
        keys = fr1.read().split('\n')
        val = fr2.read().split('\n')
        dict_out_1 = {}
        if len(keys) > len(val):
            x = len(val) - len(keys)
            for i in range(len(keys)):
                if i < len(val):
                    dict_out_1.setdefault(keys[i], val[i])
                else:
                    for g in range(x, 0):
                        i += 1
                        dict_out_1.setdefault(keys[g], None)
        elif len(val) == len(keys):
            for i in range(len(keys)):
                 dict_out_1.setdefault(keys[i], val[i])
        else:
            raise SystemExit(1)
    return  dict_out_1


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)