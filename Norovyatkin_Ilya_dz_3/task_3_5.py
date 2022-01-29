import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    # пишите реализацию своей программы здесь
    list_out = []
    for i in range(count):
        x = f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}'
        list_out.append(x)

    return list_out


print(get_jokes(2), '\n')
print(get_jokes(10))

print('\n\n')


def get_jokes_adv(count: int, flag=False) -> list:
    """Возвращает список шуток в количестве count(max колличество шуток = длине самого короткого списка)"""
     # пишите реализацию здесь
    nouns_1 = nouns.copy()
    adverbs_1 = adverbs.copy()
    adjectives_1 = adjectives.copy()

    list_out = []
    for i in range(count):
        x = f'{random.choice(nouns_1)} {random.choice(adverbs_1)} {random.choice(adjectives_1)}'
        if flag == True:
            list_2 = x.split()
            for noun in nouns_1:
                for fun in list_2:
                    if noun == fun:
                        nouns_1.remove(noun)

            for adverb in adverbs_1:
                for fun in list_2:
                    if adverb == fun:
                        adverbs_1.remove(adverb)

            for adjective in adjectives_1:
                for fun in list_2:
                    if adjective == fun:
                        adjectives_1.remove(adjective)
        list_out.append(x)

    return list_out


print(get_jokes_adv(count = 2, flag = True), '\n')
print(get_jokes_adv(count = 5, flag = True))