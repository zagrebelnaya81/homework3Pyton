'''os and sys'''
import sys
import os

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
    args = sys.argv[1:]

    function_name = os.getenv('FUNCTION')
    if len(args) < 2:
        print('We need actually 2 arguments!')
        sys.exit(2)

    functions = {
        "addition": addition,
        "subtraction": subtraction,
        "division": division,
        "multiply": multiply
    }

    if not function_name:
        function_name = 'addition'

    if function_name not in functions:
        print("Wrong function number")
        sys.exit(2)

    try:
        int(args[0])
    except (ValueError, IndexError):
        print("Wrong function arguments")
        sys.exit(2)
    try:
        int(args[1])
    except (ValueError, IndexError):
        print("Wrong function arguments")
        sys.exit(2)

    functions[function_name](int(args[0]),  int(args[1]))
    return None


if __name__ == '__main__':
    run_stuff()
