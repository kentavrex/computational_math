from solution import Solution
from lab3.helpers import check_the_break_point, get_response
from lab3.tests import Result


class Examples:
    """Class for examples show for all realized methods"""

    @staticmethod
    def greet() -> tuple[int, float, float, float]:
        systems = [
            "1) 1/x",
            "2) sin(x)/x",
            "3) x^2+2",
            "4) 2x+2",
            "5) log(x)",
            "6) (x^2 - 9)/(x - 3)"
        ]
        print("\n".join(systems))
        f = int(input("Enter the system number: ").strip())
        a = float(input("Enter the left border of the interval: ").strip())
        b = float(input("Enter the right border of the interval: ").strip())
        epsilon = float(input("Enter eps: ").strip())

        return f, a, b, epsilon

    @staticmethod
    def __get_res(solution: Solution, result):
        if not solution.has_discontinuity:
            return str(result)
        else:
            return solution.error_message

    @staticmethod
    @get_response
    def integrate_middle(f, a, b, epsilon):
        """Method of middle rectangles"""
        func = Result.get_function(f)
        if check_the_break_point(func, a) != 0 or check_the_break_point(func, b) != 0:
            raise IOError("The integral diverges")
        solution = Solution()
        result = solution.solve_middle(a, b, f, epsilon)
        return Examples.__get_res(solution=solution, result=result)

    @staticmethod
    @get_response
    def integrate_left(f, a, b, epsilon):
        """Method of left rectangles"""
        func = Result.get_function(f)
        if check_the_break_point(func, a) != 0 or check_the_break_point(func, b) != 0:
            raise IOError("The integral diverges")
        solution = Solution()
        result = solution.solve_left(a, b, f, epsilon)
        return Examples.__get_res(solution=solution, result=result)

    @staticmethod
    @get_response
    def integrate_right(f, a, b, epsilon):
        """Method of right rectangles"""
        func = Result.get_function(f)
        if check_the_break_point(func, a) != 0 or check_the_break_point(func, b) != 0:
            raise IOError("The integral diverges")
        solution = Solution()
        result = solution.solve_right(a, b, f, epsilon)
        return Examples.__get_res(solution=solution, result=result)


if __name__ == "__main__":
    f_number, a_point, b_point, eps = Examples.greet()

    res = Examples.integrate_middle(f=f_number, a=a_point, b=b_point, epsilon=eps)
    print('Method of middle rectangles')
    print(res)

    res = Examples.integrate_left(f=f_number, a=a_point, b=b_point, epsilon=eps)
    print('Method of left rectangles')
    print(res)

    res = Examples.integrate_right(f=f_number, a=a_point, b=b_point, epsilon=eps)
    print('Method of right rectangles')
    print(res)
