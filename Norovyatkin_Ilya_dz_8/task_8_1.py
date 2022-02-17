import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+\.[a-z]{2,6}')
    
    assert RE_MAIL.match(email), f'wrong email {email}'
    
    list_1 = re.split('@', email)
    parse_dict = {'username': list_1[0], 'domain': list_1[1]}
    
        
    return parse_dict


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')