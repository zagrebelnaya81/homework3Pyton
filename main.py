"""
high level support for doing this and that.
"""
import numbers


def larger_number_tow_param(first, second):
    """ Determination of the larger number out of two """
    if not isinstance(first, numbers.Number):
        return None
    if not isinstance(second, numbers.Number):
        return None
    # complex numbers we can't compare
    if is_complex(first):
        return None
    if is_complex(second):
        return None
    if first > second:
        return first
    return second


def larger_number_three_param(first, second, third):
    """  Determination of the larger number out of three """
    if not isinstance(first, numbers.Number) and not isinstance(second, numbers.Number):
        return None
        # complex numbers we can't compare
    if is_complex(first):
        return None
    if is_complex(second):
        return None
    if third < first > second:
        return first
    if third < second > first:
        return second
    return third


def absolute_value(num):
    """  The modulus of a complex number and nature number """
    if not isinstance(num, numbers.Number):
        return None
    return abs(num)


def sum_tow_numbers(first, second):
    """  displaying the sum of values on the screen """
    if not isinstance(first, numbers.Number):
        print("First parameter is not a number")
        return None
    if not isinstance(second, numbers.Number):
        print("Second parameter is not a number")
        return None
    summa = first+second
    print(summa)
    return summa


def is_or_not_positive(num):
    """  displaying on the screen whether the number is positive """
    if not isinstance(num, numbers.Number):
        print("Parameter is not a number")
        return None
    if is_complex(num):
        print("Parameter can't be complex number")
        return None
    print("positive" if num > 0 else "negative" if num < 0 else "zero")
    return "positive" if num > 0 else "negative" if num < 0 else "zero"


def is_complex(value):
    """  is param complex number """
    return (isinstance(value, complex)
            and (value.imag != 0))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result1 = larger_number_tow_param(2, 1)
    print(result1)
    result1_2 = larger_number_tow_param(-10 - 2j, -10 - 3j)
    result1_1 = larger_number_tow_param("2", 1)
    print(result1_1)
    result2 = larger_number_three_param(8, 4, 6)
    print(result2)
    result3 = absolute_value(-2000000000000000000000000000000000000)
    print(result3)
    result3_1 = absolute_value(-10-2j)
    print(result3_1)
    result3_2 = absolute_value("-10 - 2j")
    print(result3_2)
    result3_3 = absolute_value(2.1111)
    print(result3_3)
    sum_tow_numbers(-2.1111, "5")
    sum_tow_numbers(-2.1111, 5)
    sum_tow_numbers(-10 - 2j, 5)
    is_or_not_positive(-20)
    is_or_not_positive(2)
    is_or_not_positive(0)
    is_or_not_positive(-10-2j)
