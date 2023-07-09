from typing import Callable


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


def calculate_derivative(func: Callable, var: float) -> float:
    """Calculate derivative by definition of derivative"""
    d_var = 1e-7
    return (func(var + d_var) - func(var)) / d_var


def calculate_derivative_partial(
    func: Callable, variables_value: list[float]
) -> list[float]:
    """Calculate partial derivative by definition of derivative"""
    d_var = 1e-7
    res = []
    for i in range(len(variables_value)):
        vars_with_small = variables_value.copy()
        vars_with_small[i] += d_var
        diff = (func(vars_with_small) - func(variables_value)) / d_var
        res.append(diff)
    return res


def solve_by_gauss_method(A: list[list[float]], B: list[float]) -> list[float]:
    """The direct course of the Gauss method consists in the successive
    elimination of unknowns in the equations of the system being solved. Line,
    which is used to exclude unknowns is called the leading one.

    Backtracking sequentially traverses all rows in descending order
    the number of the iteration in which they were leading.

    :param A: Matrix of variables
    :type A: list[list[float]]
    :param B: Free column
    :type B: list[float]
    :return: List of roots
    :rtype: list[float]
    """
    n = len(B)
    # Direct Gauss method
    for i in range(n):
        # Reduction to the upper triangular form
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]
            B[k] += c * B[i]

    # Reverse Gauss method
    answer = [0] * n
    for i in range(n - 1, -1, -1):
        answer[i] = B[i]
        for j in range(i + 1, n):
            answer[i] -= A[i][j] * answer[j]
        try:
            answer[i] /= A[i][i]
        except Exception:
            pass
    return answer
