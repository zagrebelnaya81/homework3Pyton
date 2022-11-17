"""
high level support for doing this and that.
"""

import random

i = 0


def print_square(length: int):
    """ Function will display a square of the given size on the screen """
    global i

    # Plint говорит что нельзя допускать глобальные переменные.
    # Пыталась сделать по правильному классом. Но не знаю как
    # сделать рекурсию в  функции если она в классе
    # файл functions_class. Ошибка print_square() takes 2 positional
    # arguments but 3 were given
    # Думаю что функцию можно было сделать лучше, но это пока все на что
    # я способна в питоне:)))))))))))))))))))

    if length == 1:
        print("*")
        return
    if length == 2:
        print("*"*4)
        return
    if i == 0:
        print("* " * length)
    print("* " + "  " * (length-2) + "*")
    if i == length-3:
        print("* " * length)
    i = i+1
    if i < length-2:
        print_square(length)


# decoration  function
def retry(attempts: int = 5, desired_value: any = None):
    """ A retry function that will repeat some code a specified number of times"""

    def retry_decorator(func):
        """ A retry function that  get func"""
        def wrapper(*args, **kwargs):
            """ A retry function that  get arg func"""
            for _ in range(attempts):
                result = func(*args, **kwargs)
                if result == desired_value:
                    return result
            print("It was not possible to achieve the desired value")
            return None
        return wrapper

    return retry_decorator


@retry(desired_value=3)
def get_random_value():
    """ A function that get random value"""
    return random.choice((1, 2, 3, 4, 5))


@retry(desired_value=[1, 2])
def get_random_values(choices, size=2):
    """ A function that get random value with size"""
    return random.choices(choices, k=size)

#
# @retry(attempts=7, desired_value=3)
# def get_random_value():
#     """ A function that get random value"""
#     return random.choice((1, 2, 3, 4, 5))
#
#
# @retry(attempts=2, desired_value=[1, 2, 3])
# def get_random_values(choices, size=2):
#     """ A function that get random value with size"""
#     return random.choices(choices, k=size)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_square(7)
    result1 = get_random_value()
    print(result1)
    result2 = get_random_values([1, 2, 3, 4])
    print(result2)
    result3 = get_random_values([1, 2, 3, 4], 3)
    print(result3)
    result4 = get_random_values([1, 2, 3, 4], size=1)
    print(result4)
