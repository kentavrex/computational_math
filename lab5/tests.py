import math


def first_function(x: float, y: float):
    return math.sin(x)


def second_function(x: float, y: float):
    return (x * y) / 2


def third_function(x: float, y: float):
    return x - y + 3


def get_function(n: int):
    if n == 1:
        return first_function
    elif n == 2:
        return second_function
    elif n == 3:
        return third_function
    else:
        return 0
