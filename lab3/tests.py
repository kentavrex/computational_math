#!/bin/python3

import math
from typing import Callable


class Result:
    error_message = ""
    has_discontinuity = False

    def first_function(x: float):
        return 1 / x

    def second_function(x: float):
        return math.sin(x) / x

    def third_function(x: float):
        return x * x + 2

    def fourth_function(x: float):
        return 2 * x + 2

    def five_function(x: float):
        return math.log(x)

    def six_function(x: float):
        return (x**2 - 9) / (x - 3)

    # How to use this function:
    # func = Result.get_function(4)
    # func(0.01)
    def get_function(n: int) -> Callable:
        if n == 1:
            return Result.first_function
        elif n == 2:
            return Result.second_function
        elif n == 3:
            return Result.third_function
        elif n == 4:
            return Result.fourth_function
        elif n == 5:
            return Result.five_function
        elif n == 6:
            return Result.six_function
        else:
            raise NotImplementedError(f"Function {n} not defined.")
