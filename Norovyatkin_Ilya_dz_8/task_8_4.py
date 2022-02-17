def def_arg(a):
    return type(a)==int and a > 0
    
def val_checker(b):    
    def _val_checker(func):
        def wrapper(c):
            if b(c):
                result = func(c)
            else:
                msg = f'wrong val {c}'
                raise ValueError(msg)

            return result

        return wrapper

    return _val_checker

@val_checker(def_arg)  # не забудьте про аргумент-функцию
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3

print(calc_cube(5))
print(calc_cube('ss'))
