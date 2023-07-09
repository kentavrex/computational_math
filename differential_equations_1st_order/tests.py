import math


def first_function(x: float, y: float):
    return (x / y) * 4


def second_function(x: float, y: float):
    return math.cos(x)


def third_function(x: float, y: float):
    return x - y + 7


def get_function(n: int):
    if n == 1:
        return first_function
    elif n == 2:
        return second_function
    elif n == 3:
        return third_function
    else:
        return 0

def const_for_first_analytical(x: float, y: float):
    return y - 2*(x**2)/y


def const_for_second_analytical(x: float, y: float):
    return y - math.sin(x)


def const_for_third_analytical(x: float, y: float):
    return y - (x**2)/2 + x*y - 7*x


def analytical_first(x: float, y: float, c: float):
    return 2*(x**2)/y + c


def analytical_second(x: float, y: float, c: float):
    return math.sin(x) + c


def analytical_third(x: float, y: float, c: float):
    return (x**2)/2 - x*y + 7*x + c