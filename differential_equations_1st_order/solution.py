from matplotlib import pyplot as plt

from differential_equations_1st_order.tests import get_function, const_for_first_analytical, const_for_second_analytical, const_for_third_analytical, analytical_first, analytical_second, analytical_third



class Solution:
    @staticmethod
    def get_analytical_and_const(n: int):
        if n == 1:
            return analytical_first, const_for_first_analytical
        elif n == 2:
            return analytical_second, const_for_second_analytical
        elif n == 3:
            return analytical_third, const_for_third_analytical

    @staticmethod
    def get_analytical_solve(f, y0, x0, x1) -> tuple[list[float], list[[float]]]:
        h = 0.1
        func, const_func = Solution.get_analytical_and_const(f)
        c = const_func(x0, y0)
        list_x = [x0]
        list_y = [func(x0, y0, c)]

        x = x0 + h
        list_x.append(round(x, 4))
        y = func(list_x[-1], list_y[-1], c)
        list_y.append(y)

        while x < x1:   # проходимся по отрезку
            list_x.append(round(x, 4))
            y = func(list_x[-1], list_y[-1], c)
            x += h
            list_y.append(y)

        return list_x, list_y

    @staticmethod
    def __runge_kutt_method(
            func, x0: float, y0: float, h: float
    ) -> tuple[list[float], list[float]]:
        """Get the first 4 points by Runge-Kutt method"""
        x_axis, y_axis = [x0], [y0]
        count_of_needed_vars = 3
        for i in range(count_of_needed_vars):
            x, y = x_axis[i], y_axis[i]
            k1 = h * func(x, y)

            x = x_axis[i] + h / 2
            y = y_axis[i] + h / 2 * k1
            k2 = h * func(x, y)

            y = y_axis[i] + h / 2 * k2
            k3 = h * func(x, y)

            x = x_axis[i] + h
            y = y_axis[i] + h * k3
            k4 = h * func(x, y)

            x_new = x_axis[i] + h
            y_new = y_axis[i]
            y_new += 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

            x_axis.append(x_new)
            y_axis.append(y_new)

        return x_axis, y_axis

    @staticmethod
    def make_graphic(f, x0, x1, x_axis, y_axis, y0) -> None:
        plt.plot(x_axis, y_axis, "k", label='Численное решение')
        plt.plot(x_axis[0], y_axis[0], 'ro', label='Начальная точка')
        x_analytic, y_analytic = Solution.get_analytical_solve(f, y0, x0, x1)
        plt.plot(x_analytic, y_analytic, "b", label='Аналитическое решение')
        # Строим график аналитического решения, если оно задано
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

    @staticmethod
    def solveByMilne(f, epsilon, a, y_a, b):    # noqa
        """Milne multi-step method of solving Koshi task"""
        x0, x1, y0 = a, b, y_a
        func = get_function(f)
        h = 0.1     # step

        x_axis, y_axis = Solution.__runge_kutt_method(
            func=func, x0=x0, y0=y0, h=h
        )

        new_x = x_axis[-1] + h
        while new_x <= b:
            y_predicted = y_axis[-4]
            tmp_in = 2 * func(x_axis[-1], y_axis[-1])
            tmp_in -= func(x_axis[-2], y_axis[-2])
            tmp_in += 2 * func(x_axis[-3], y_axis[-3])
            y_predicted += 4/3 * h * tmp_in

            while True:
                new_f = func(new_x, y_predicted)
                y_corrected = y_axis[-2]
                tmp_in = new_f
                tmp_in += 4 * func(x_axis[-1], y_axis[-1])
                tmp_in += func(x_axis[-2], y_axis[-2])
                y_corrected += 1/3 * h * tmp_in

                if abs(y_corrected - y_predicted) <= epsilon:
                    break
                else:
                    y_predicted = y_corrected

            x_axis.append(new_x)
            y_axis.append(y_corrected)
            new_x = x_axis[-1] + h

        Solution.make_graphic(f=f, x0=x0, x1=x1, x_axis=x_axis, y_axis=y_axis, y0=y0)

        return y_axis[-1]
