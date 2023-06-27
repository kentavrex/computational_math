from matplotlib import pyplot as plt
import equations
import numpy as np

def draw(a, b, y, n):

    x = np.linspace(a, b, len(y))
    y_old = []

    for i in range(len(x)):
        y_old.append(equations.get_analytic(n, x[i]))

    plt.plot(x, y_old, 'b', label='Аналитическое решение')
    plt.plot(x, y, 'r', label='Решение методом пристрелки')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
