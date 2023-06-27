import numpy as np
from matplotlib import pyplot as plt


class Solution:
    @staticmethod
    def __get_polynomial(x, x_axis, i):
        polynomial = 1
        for j, xj in enumerate(x_axis):
            if j != i:
                polynomial *= (x - xj)
                polynomial /= (x_axis[i] - xj)
        return polynomial

    @staticmethod
    def interpolate_by_lagrange(x_axis, y_axis, x) -> float:
        point_y = 0
        for y_axis_index, y_val in enumerate(y_axis):
            polynomial = Solution.__get_polynomial(
                x=x, x_axis=x_axis, i=y_axis_index
            )
            point_y += y_val * polynomial
        return point_y

    @staticmethod
    def plot_interpolate(x_axis, y_axis, x, result):
        # Create points data to create a graphic
        x_values = np.linspace(min(x_axis), max(x_axis), 100)
        y_value = [Solution.interpolate_by_lagrange(x_axis, y_axis, xi) for xi in x_values]

        # Create a line in graphic
        plt.plot(x_values, y_value, label='Interpolation', linewidth=5)

        # Add input data points to graphic and interpolated point
        plt.plot(x_axis, y_axis, 'ko', label='Data Points')
        plt.plot(x, result, 'ro', label='Interpolated Point')

        plt.legend()
        plt.show()
