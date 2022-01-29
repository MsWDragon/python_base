def thesaurus(*args) -> dict:
    # пишите свою реализацию здесь
    dict_out_1 = {}
    for n in args:
        if n[0] in dict_out_1:
            a = dict_out_1[n[0]] 
            a = a.append(f'{n}')
        else:
            dict_out_1.setdefault (n[0], [n])
    dict_out = dict_out_1
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))


def thesaurus_adv(*args) -> dict:
    # пишите свою реализацию здесь
    dict_out_2 = {}
    for n in args:
        x = n.split()
        y = x[1]
        name_ = thesaurus(x[0])
        if y[0] in dict_out_2:
            a = dict_out_2[y[0]] 
            a = a.update(name_)
        else:
            dict_out_2.setdefault (y[0], name_)
    dict_out_adv = dict_out_2
    return dict_out_adv


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))