from typing import Callable

from helpers import (
    get_response,
    calculate_derivative,
    calculate_derivative_partial,
    solve_by_gauss_method,
)
from vychmat.lab2.tests_for_system_solve import get_functions


class Solution:
    @staticmethod
    @get_response
    def chord_method(
        func: Callable[[float], float], segment: tuple[float, float], eps: float
    ) -> tuple[float, int]:
        """This function implements the chord method for finding the root of the equation
        func(x) = 0 on the interval [a, b] with the given precision eps

        :param func: Func, root should we find
        :type func: Callable[[float], float]
        :param segment: Line segment where is root
        :type segment: tuple[float, float]
        :param eps: Accuracy
        :type eps: float
        :return: Root of func and count of iters
        :rtype: tuple[float, int]
        """

        chord_method_func: Callable[[float], float] = lambda left, right: (
            left * func(right) - right * func(left)
        ) / (func(right) - func(left))

        def _change_interval(left: float, right: float) -> tuple[float, float, float]:
            """Helper func to change the interval and get new xi"""
            x = round(chord_method_func(left, right), 10)
            if func(x) * func(left) < 0:
                right = x
            else:
                left = x
            return x, left, right

        a, b = segment[0], segment[-1]
        iter_counter, xn_prev = 0, 0
        xi = None

        if func(a) * func(b) < 0:
            while abs(a - b) > eps:
                xn_prev = xi or 0
                xi, a, b = _change_interval(a, b)
                if abs(xi - xn_prev) <= eps or abs(func(xi)) <= eps:
                    break
                iter_counter += 1

                if iter_counter > 100000:
                    raise IOError("There are probably incorrect inputs")
        return xi, iter_counter

    @staticmethod
    @get_response
    def tangent_method(
        func: Callable[[float], float], segment: tuple[float, float], eps: float
    ) -> tuple[float, int]:
        """This function implements the tangent method for finding the root of the equation
        func(x) = 0 on the interval [a, b] with the given precision eps.

        :param func: Func, root should we find
        :type func: Callable[[float], float]
        :param segment: Line segment where is root
        :type segment: tuple[float, float]
        :param eps: Accuracy
        :type eps: float
        :return: Root of func and count of iters
        :rtype: tuple[float, int]
        """

        def helper(var: float) -> float:
            x = var
            var_derivative = calculate_derivative(func=func, var=var)
            x -= func(var) / var_derivative
            return x

        a, b = segment[0], segment[-1]
        iter_counter = 0
        xi = None

        if func(a) * func(b) < 0:  # Convergence condition
            while True:
                x_prev = xi or 0
                xi = helper(x_prev)
                x_derivative = calculate_derivative(func=func, var=xi)
                if (
                    abs(xi - x_prev) <= eps
                    or abs(func(xi) / x_derivative) <= eps
                    or abs(func(xi)) <= eps
                ):
                    break
                iter_counter += 1

                if iter_counter > 100000:
                    raise IOError("There are probably incorrect inputs")
        return xi, iter_counter

    @staticmethod
    @get_response
    def solve_by_fixed_point_iterations(
        system_id, number_of_unknowns, initial_approximations
    ) -> list[float]:
        """Newton method realization of non-linear system

        :param system_id: Id of system
        :type system_id: int
        :param number_of_unknowns: Number of unknowns
        :type number_of_unknowns: int
        :param initial_approximations: List of initial approximations
        :type initial_approximations: list[float
        :return: System roots
        :rtype: list[float]
        """
        return SystemSolveNewton.solve_by_fixed_point_iterations(
            system_id, number_of_unknowns, initial_approximations
        )


class SystemSolveNewton:
    """Class for Newton method realization of non-linear system logic"""
    @staticmethod
    def _make_jacobian(
        functions: list[Callable], variables_value: list[float]
    ) -> list[list[float]]:
        """Calculate Jacobian

        :param functions: Function
        :type functions: list[Callable]
        :param variables_value: List of initial approximations
        :param variables_value: list[float]
        :return: Jacobian
        :rtype: list[list[float]]
        """
        matrix_jacobian = [[0] * len(variables_value)] * len(variables_value)
        for i, func in enumerate(functions):
            matrix_jacobian[i] = calculate_derivative_partial(
                func=func, variables_value=variables_value
            )
        return matrix_jacobian

    @staticmethod
    def _get_free_column(functions, variables_value) -> list[float]:
        """Get free column for matrix

        :param functions: Function
        :type functions: list[Callable]
        :param variables_value: List of initial approximations
        :param variables_value: list[float]
        :return: Free column for matrix
        :rtype: list[list[float]]
        """
        return [(-1) * func(variables_value) for func in functions]

    @staticmethod
    def _calculate_matrix(functions, variables_value) -> list[float]:
        """Calculate matrix

        :param functions: Function
        :type functions: list[Callable]
        :param variables_value: List of initial approximations
        :param variables_value: list[float]
        :return: Free column for matrix
        :rtype: list[list[float]]
        """
        jacobian = SystemSolveNewton._make_jacobian(
            functions=functions, variables_value=variables_value
        )
        free_column = SystemSolveNewton._get_free_column(
            functions=functions, variables_value=variables_value
        )
        return solve_by_gauss_method(A=jacobian, B=free_column)

    @staticmethod
    def solve_by_fixed_point_iterations(
        system_id: int, number_of_unknowns: int, initial_approximations: list[float]
    ) -> list[float]:
        """Newton method realization of non-linear system

        :param system_id: Id of system
        :type system_id: int
        :param number_of_unknowns: Number of unknowns
        :type number_of_unknowns: int
        :param initial_approximations: List of initial approximations
        :type initial_approximations: list[float
        :return: System roots
        :rtype: list[float]
        """
        eps = 0.001
        functions: list[Callable] = get_functions(system_id)
        answer: list[float]
        while True:
            answer = SystemSolveNewton._calculate_matrix(
                functions=functions, variables_value=initial_approximations
            )
            for i in range(len(answer)):
                initial_approximations[i] += answer[i]
            if max(answer) <= eps:
                break
        return initial_approximations
