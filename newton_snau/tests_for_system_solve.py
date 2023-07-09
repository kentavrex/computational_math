#!/bin/python3

import math
import os
import random
import re
import sys

k = 0.4
a = 0.9


# 1) sin(x)
# 2) x*y/2
# 3) tan(x*y+0.4)-x²
# 4) 0.9*x²+2*y²-1
# 5) x²+y²+z²-1
# 6) 2*x²+y²-4*z
# 7) 3*x²-4*y+z²
def first_function(args: []) -> float:
    return math.sin(args[0])


def second_function(args: []) -> float:
    return (args[0] * args[1]) / 2


def third_function(args: []) -> float:
    return math.tan(args[0] * args[1] + k) - pow(args[0], 2)


def fourth_function(args: []) -> float:
    return a * pow(args[0], 2) + 2 * pow(args[1], 2) - 1


def fifth_function(args: []) -> float:
    return pow(args[0], 2) + pow(args[1], 2) + pow(args[2], 2) - 1


def six_function(args: []) -> float:
    return 2 * pow(args[0], 2) + pow(args[1], 2) - 4 * args[2]


def seven_function(args: []) -> float:
    return 3 * pow(args[0], 2) - 4 * args[1] + pow(args[2], 2)


def default_function(args: []) -> float:
    return 0.0


# How to use this function:
# funcs = Result.get_functions(4)
# funcs[0](0.01)
# 1) sin(x)
# 2) x*y/2
# 3) tan(x*y+0.4)-x²
# 4) 0.9*x²+2*y²-1
# 5) x²+y²+z²-1
# 6) 2*x²+y²-4*z
# 7) 3*x²-4*y+z²
def get_functions(n: int):
    # sin(x)
    # x*y/2
    if n == 1:
        return [first_function, second_function]
    # tan(x*y+0.4)-x²
    # 0.9*x²+2*y²-1
    elif n == 2:
        k = 0.4
        a = 0.9
        return [third_function, fourth_function]
    # tan(x*y)-x²
    # 0.5*x²+2*y²-1
    elif n == 3:
        k = 0
        a = 0.5
        return [third_function, fourth_function]
    # x²+y²+z²-1
    # 2*x²+y²-4*z
    # 3*x²-4*y+z²
    elif n == 4:
        return [fifth_function, six_function, seven_function]
    else:
        return [default_function]
