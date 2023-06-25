import numpy as np
from matplotlib import pyplot as plt


class Solution:
    @staticmethod
    def __get_polynomial(x, x_axis, y_axis_index):
        polynomial = 1
        for x_axis_index, x_val in enumerate(x_axis):
            if x_axis_index != y_axis_index:
                polynomial *= (x - x_val)
                polynomial /= (x_axis[y_axis_index] - x_val)
        return polynomial

    @staticmethod
    def interpolate_by_lagrange(x_axis, y_axis, x):
        res = 0
        for y_axis_index, y_val in enumerate(y_axis):
            polynomial = Solution.__get_polynomial(
                x=x, x_axis=x_axis, y_axis_index=y_axis_index
            )
            res += y_val * polynomial
        return res

    @staticmethod
    def plot_interpolate(x_axis, y_axis, x, result):
        # создаем массив точек для построения графика
        x_value = np.linspace(min(x_axis), max(x_axis), 100)
        y_value = [Solution.interpolate_by_lagrange(x_axis, y_axis, xi) for xi in x_value]

        # рисуем график
        plt.plot(x_value, y_value, label='Interpolation', linewidth=5)

        # добавляем исходные точки и точку интерполяции
        plt.plot(x_axis, y_axis, 'o', label='Data Points')
        plt.plot(x, result, 'ro', label='Interpolated Point')

        plt.legend()
        plt.show()
