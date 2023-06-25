from typing import Callable

from vychmat.lab3.helpers import calculate_integral, get_value, get_sign, check_the_break_point
from vychmat.lab3.tests import Result


class Solution(Result):
    @staticmethod
    def __get_option(point: float) -> int:
        offer = f'In interval was found 1 type of dot divergence ≈ {point}, ' \
                f'please choose the option [1/2]:\n' \
                f'Option 1: ignore the point and calculate 2 integrals\n' \
                f'Option 2: f(x) = (f(x - dx) + f(x + dx)) / 2'
        print(offer)
        option = input('Enter the option: ').strip()
        while not (option == '1' or option == '2'):
            option = input('Enter the correct option [1/2]: ').strip()
        return int(option)

    @staticmethod
    def __research_dot_type(dot_type: int, point: float, func: Callable) -> float:
        add_to_sum_value = 0
        match dot_type:
            case 3:
                raise ValueError("Break point type 1, fatal")
            case 2:
                raise ValueError("Break point type 2")
            case 1:
                option = Solution.__get_option(point=point)
                while not (option == 1 or option == 2):
                    option = input('Enter the correct option [1/2]: ').strip()
                match option:
                    case 1:
                        add_to_sum_value = 0
                    case 2:
                        dx = 1e-10
                        add_to_sum_value = (func(point - dx) + func(point + dx)) / 2
        return add_to_sum_value

    @staticmethod
    def solve_middle(
            a: float, b: float, f: int, epsilon: float
    ) -> tuple[float | None, float | None]:
        func: Callable = Result.get_function(f)
        true_result = calculate_integral(func=func, left_end=a, right_end=b)

        sign, a, b = get_sign(a, b)
        n = int((b - a) / epsilon)
        sum_of_integral = 0
        step = (b - a) / n
        for _ in range(n):
            point = a + step / 2
            dot_type = check_the_break_point(func, round(a, 10))
            result = get_value(func=func, point=point)
            if str(result) != 'nan' and dot_type == 0:
                sum_of_integral += result
                a += step
                continue

            try:
                sum_of_integral += Solution.__research_dot_type(
                    dot_type=dot_type,
                    point=point,
                    func=func
                )
                a += step
            except ValueError as e:
                raise ValueError(e)

        fault = abs(true_result - sum_of_integral * step)
        answer = sum_of_integral * step, fault
        if sign == 1:
            answer = -1 * sum_of_integral * step, fault

        return answer

    @staticmethod
    def solve_left(
            a: float, b: float, f: int, epsilon: float
    ) -> tuple[float | None, float | None]:
        func: Callable = Result.get_function(f)
        true_result = calculate_integral(func=func, left_end=a, right_end=b)

        sign, a, b = get_sign(a, b)
        n = int((b - a) / epsilon)
        sum_of_integral = 0
        step = (b - a) / n
        for _ in range(n):
            point = a + step
            dot_type = check_the_break_point(func, round(a, 10))
            result = get_value(func=func, point=point)
            if str(result) != 'nan' and dot_type == 0:
                sum_of_integral += result
                a += step
                continue

            try:
                sum_of_integral += Solution.__research_dot_type(
                    dot_type=dot_type,
                    point=point,
                    func=func
                )
                a += step
            except ValueError as e:
                raise ValueError(e)

        fault = abs(true_result - sum_of_integral * step)
        answer = sum_of_integral * step, fault
        if sign == 1:
            answer = -1 * sum_of_integral * step, fault

        return answer

    @staticmethod
    def solve_right(
            a: float, b: float, f: int, epsilon: float
    ) -> tuple[float | None, float | None]:
        func: Callable = Result.get_function(f)
        true_result = calculate_integral(func=func, left_end=a, right_end=b)

        sign, a, b = get_sign(a, b)
        n = int((b - a) / epsilon)
        sum_of_integral = 0
        step = (b - a) / n
        for _ in range(n):
            point = b - step
            dot_type = check_the_break_point(func, round(b, 10))
            result = get_value(func=func, point=point)
            if str(result) != 'nan' and dot_type == 0:
                sum_of_integral += result
                b -= step
                continue

            try:
                sum_of_integral += Solution.__research_dot_type(
                    dot_type=dot_type,
                    point=point,
                    func=func
                )
                b -= step
            except ValueError as e:
                raise ValueError(e)

        fault = abs(true_result - sum_of_integral * step)
        answer = sum_of_integral * step, fault
        if sign == 1:
            answer = -1 * sum_of_integral * step, fault

        return answer
