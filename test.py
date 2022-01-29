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
    dict_out_3 = {}
    for n_1 in args:
        x = n_1.split()
        y = x[1]
        if y[0] in dict_out_3:
            b = dict_out_3[y[0]] 
            b = b.append(f'{n_1}')
        else:
            dict_out_3.setdefault (y[0], [n_1])
    for key in dict_out_3:
        dict_out_3[key] = thesaurus(",".join([str(i) for i in dict_out_3[key]]))
    dict_out_adv = dict_out_3
    return dict_out_adv


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "И": {
        "И": ["Илья Иванов"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"], 
        "А": ["Анна Савельева"]
    }
}