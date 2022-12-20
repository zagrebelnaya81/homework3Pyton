'''os and sys'''
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
    parser.add_argument(
        '--function_number',
        type=str,
        default='1',
        help='provide an integer (default: 1)'
    )
    args = parser.parse_args()

    if not args.first or not args.second:
        print('We need actually 2 arguments!')
        sys.exit(2)
    try:
        if isinstance(args.first, int):
            return args.first
    except (ValueError, IndexError, TypeError) as e:
        print(e)
    raise argparse.ArgumentTypeError('%s is not a valid argument' % (args.first,))

    try:
        if isinstance(args.second, int):
            return args.second
    except (ValueError, IndexError, TypeError) as e:
        print(e)
    raise argparse.ArgumentTypeError('%s is not a valid argument' % (args.second,))

    functions = {
        "1": addition,
        "2": subtraction,
        "3": division,
        "4": multiply
    }

    function_number = args.function_number

    if function_number not in functions:
        print("Wrong function number")
        sys.exit(2)

    functions[function_number](args.first, args.second)


if __name__ == '__main__':
    run_stuff()
