import math


def first_function_derivative_2(x, y, y1):  # Change to analytic view
    return x ** 4


def first_function_derivative(x, c1):  # Change to analytic view
    return x ** 5 / 5 + c1


def first_function(x, c1, c2):
    return x ** 6 / 30 + c1 * x + c2


def get_function(n: int):
    if n == 1:
        return first_function
    else:
        return 0
