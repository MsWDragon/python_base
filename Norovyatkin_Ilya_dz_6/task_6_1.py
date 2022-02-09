from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    line = line.split(' ', 7)
    addr = line[0]
    req_type = line[5].split('"', 1)[1]
    req_res = line[6]
    return  (addr, req_type, req_res)


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        list_out.append(get_parse_attrs(line))

pprint(list_out[:5])