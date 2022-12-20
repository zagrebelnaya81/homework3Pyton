'''os and sys'''
import sys


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
    function_number = None
    if len(args) < 2:
        print('We need actually 2 arguments!')
        sys.exit(2)

    functions = {
        "1": addition,
        "2": subtraction,
        "3": division,
        "4": multiply
    }
    firstvar = args[0]
    secondvar = args[1]
    if len(args) == 2:
        function_number = '1'
    else:
        function_number = args[2]

    if not isinstance(firstvar, int) or not isinstance(secondvar, int):
        print("Wrong function arguments")
        sys.exit(2)

    firstarg = int(firstvar)
    secondarg = int(secondvar)



    if function_number not in functions:
        print("Wrong function number")
        sys.exit(2)

    functions[function_number](firstarg, secondarg)


if __name__ == '__main__':
    run_stuff()
