def type_logger(func):

    def wrapper(*args, **kwargs):
        list_1 = []
        for b in args:
            x = f'{b} : {type(b)}'
            list_1.append(x)
        for c in kwargs:
            y = f'{kwargs[c]} : {type(kwargs[c])}'
            list_1.append(y)
        print(",".join(map(str, list_1)))
        result = func(*args, **kwargs)

        return result

    return wrapper


@type_logger
def calc_cube(*args, **kwargs):
    list_2 = []
    for d in args:
        result = d ** 3
        list_2.append(result)
    for e in kwargs:
        result = kwargs[e] ** 3
        list_2.append(result)
    return (",".join(map(str, list_2)))
    


a = calc_cube(5, 3, first = 6, second = 8)
print(a)