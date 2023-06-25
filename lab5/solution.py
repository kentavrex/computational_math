from lab5.tests import get_function


class Solution:
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
    def solveByMilne(f, epsilon, a, y_a, b):    # noqa
        """Milne multi-step method of solving Koshi task"""
        x0, y0 = a, y_a
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

        return y_axis[-1]
