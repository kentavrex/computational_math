from typing import Callable

from sympy import Symbol, integrate


def get_response(func):
    """Get result of call func"""

    def wrapper(*args, **kwargs):
        data = {}
        try:
            data["message"] = func(*args, **kwargs)
            status = 200
        except Exception as e:
            data["error"] = str(e)
            status = 500
        return {"data": data, "status": status}

    return wrapper


def calculate_integral(func, left_end, right_end):  # TODO Delete for Code&Test. For check
    try:
        x = Symbol("x")
        y = func(x).diff(x, 0)
        return integrate(y, (x, left_end, right_end))
    except:
        return "Library check is unavailable"


def get_value(func, point):
    try:
        res = func(point)
    except (ZeroDivisionError, ValueError):
        res = 'nan'
    return res


def get_sign(a, b):
    sign = 0
    if a > b:
        a, b = b, a
        sign = 1
    return sign, a, b


def check_the_break_point(func: Callable, val: float) -> int:
    """
    0 - НЕ точка разрыва
    1 - точка разрыва 1 рода, устранимая
    2 - точка разрыва 1 рода, неустранимая
    3 - точка разрыва 2 рода = всегда неустранимая
    """
    dx = 1e-10
    inf = 1e10

    value = get_value(func=func, point=val)
    left_lim = get_value(func=func, point=(val-dx))
    right_lim = get_value(func=func, point=(val+dx))

    if str(value) == 'nan':
        if abs(left_lim) >= inf or abs(right_lim) >= inf or str(left_lim) == 'nan' or str(right_lim) == 'nan':
            return 2

        if left_lim == right_lim:
            return 1
        else:
            return 3

    return 0
