import requests
import sys
from pyquery import PyQuery as pq
from lxml import etree


url = 'http://www.cbr.ru/scripts/XML_daily.asp'


def send_request() -> requests.Response:
    """Выполняет запрос данных с ЦБР"""
    response = requests.get(url, timeout=2)
    if not response.ok:
        print(f'Запрос не успешен: {response.status_code}')
        sys.exit(0)
    return response


def currency_rates(code: str) -> float:
    #Извлекает данные и возвращает курс валюты `code` по отношению к рублю
    code_1 = code.upper()
    res = send_request()
    main_root = pq(etree.fromstring(res.content))
    curs_val = main_root.pop()
    char_code = curs_val.xpath(f'//Valute/CharCode/text()')
    value = curs_val.xpath(f'//Valute/Value/text()')
    nominal = curs_val.xpath(f'//Valute/Nominal/text()')
    v = {}
    idx = 0
    for i in value:
        curs = float(value[idx].replace(',','.')) / float(nominal[idx].replace(',','.'))
        v.setdefault(char_code[idx], curs)
        idx += 1
    if code_1 in v:
        x = v[code_1]
    else:
        x = 'None'
    return x


if __name__ == '__main__':

    print(currency_rates("uSd"))
    print(currency_rates("eur"))