from typing import Callable

import numpy as np
from matplotlib import pyplot as plt

from differential_equations_2st_order import tests


class Solution:

    @staticmethod
    def shooting_method(a, b, ya, yb, eps, f_num):
        n = 50 * 15
        p, q, f = tests.get_pqf(f_num)
        while True:
            h = (b - a) / n
            x = np.linspace(a, b, n + 1)
            y = [[ya, ya + h], [0, h]]
            for i in range(1, n):
                y[0].append(
                    (
                    (h ** 2 * f(x[i]) - (1.0 - (h / 2) * p(x[i])) * y[0][i - 1] - (h ** 2 * q(x[i]) - 2) * y[0][i])) / (
                            1 + h / 2 * p(x[i])))
                y[1].append(
                    (-(1 - h / 2 * p(x[i])) * y[1][i - 1] - (h ** 2 * q(x[i]) - 2) * y[1][i]) / (1 + h / 2 * p(x[i])))
            y_numerical = []
            for i in range(n + 1):
                c1 = ((yb - y[0][n]) / y[1][n])
                y_numerical.append(y[0][i] + c1 * y[1][i])
            if abs(y_numerical[-1] - yb) < eps:
                return y_numerical

    @staticmethod
    def draw(a, b, y_numerical, ya, yb, f_num):
        x = np.linspace(a, b, len(y_numerical))
        y_analytical = []
        for i in range(len(x)):
            y_analytical.append(tests.get_analytical_solve(f_num=f_num, x=x[i], ya=ya, yb=yb, a=a, b=b))

        plt.plot(x, y_analytical, "ro", label="Analytical solution")
        plt.plot(x, y_numerical, "b", label="Numerical solution")
        plt.plot([a, b], [ya, yb], "bo")
        plt.grid(True)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.show()

