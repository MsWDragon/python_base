'''def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
    translate = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять'
    }
    str_out = translate.get(value)
    return str_out


print(num_translate("ten"))
print(num_translate("two"))'''


def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
    translate = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять'
    }
    str_out_1 = ''
    if value.istitle():
        value = value.lower()
        str_out_1 = f'{translate.get(value)}'.capitalize()
    else:
        str_out_1 = translate.get(value)
    str_out = str_out_1
    return str_out


print(num_translate_adv("Five"))
print(num_translate_adv("Eleven"))