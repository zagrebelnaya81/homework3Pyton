'''os and sys'''
import os
import sys
import argparse


def addition(first: int, second: int):
    ''' addition '''
    print(first+second)


def subtraction(first: int, second: int):
    ''' subtraction '''
    print(first-second)


def division(first: int, second: int):
    ''' division '''
    try:
        print(first / second)
    except ZeroDivisionError:
        print("Division by zero")


def multiply(first: int, second: int):
    ''' multiply '''
    print(first * second)


def run_stuff():
    '''run all staff'''
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", type=int,
                        help="first variable")
    parser.add_argument("--second", type=int,
                        help="second variable")

    args = parser.parse_args()

    if not args.first or not args.second:
        print('We need actually 2 arguments!')
        sys.exit(2)

    # У меня вопрос. Смотрите, я пытаюсь разобраться с библиотекой
    # argparse. Для того чтоб обрабатывать самой
    # ошибки количества параметров и тд я сделала их всех опциональными
    # так как при недостаточном вводе параметров библиотека
    # дает ошибки, что не хватает параметров и тд.
    # Пытаюсь проверить на тип параметров, библиотека выдает ошибку.
    # Но почему-то не ловит мой обработчик
    # ошибок. Не очень понимаю как здесь отловить эти ошибки правильно
    try:
        if isinstance(args.first, int):
            return args.first
    except (ValueError, IndexError, TypeError):
        print("Wrong function arguments")
        sys.exit(2)

    try:
        if isinstance(args.second, int):
            return args.second
    except (ValueError, IndexError, TypeError):
        print("Wrong function arguments")
        sys.exit(2)

    functions = {
        "addition": addition,
        "subtraction": subtraction,
        "division": division,
        "multiply": multiply
    }

    function_name = os.getenv("FUNCTION")
    print(function_name)
    if not function_name:
        function_name = 'addition'

    if function_name not in functions:
        print("Wrong function number")
        sys.exit(2)

    functions[function_name](args.first, args.second)
    return None


if __name__ == '__main__':
    run_stuff()
