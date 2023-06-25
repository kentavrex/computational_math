import math
import matplotlib.pyplot as plt


def const_first(x: float, y: float):
    return y + math.cos(x)


def const_second(x: float, y: float):
    return y / (math.e ** (x ** 2 / 4))


def const_third(x: float, y: float):
    return (y - x - 2) * (math.e ** x)


def analit_first(x: float, y: float, c: float):
    return (math.cos(x) * -1) + c


def analit_second(x: float, y: float, c: float):
    return math.e ** (x ** 2 / 4) * c


def analit_third(x: float, y: float, c: float):
    return (c / (math.e ** x)) + x + 2


def first_function(x: float, y: float):
    return math.sin(x)


def second_function(x: float, y: float):
    return (x * y) / 2


def third_function(x: float, y: float):
    return x - y + 3


def get_function(n: int):
    if n == 1:
        return first_function
    elif n == 2:
        return second_function
    elif n == 3:
        return third_function
    else:
        return 0


def get_analytical_const(n: int):
    if n == 1:
        return analit_first, const_first
    elif n == 2:
        return analit_second, const_second
    elif n == 3:
        return analit_third, const_third

def analytical(f, y_a, a, b):
    h = 0.1
    fun, const_fun = get_analytical_const(f)
    c = const_fun(a, y_a)
    list_x = [a]
    list_y = [fun(a, y_a, c)]

    x = a + h
    list_x.append(round(x, 4))
    y = fun(list_x[-1], list_y[-1], c)
    list_y.append(y)
    x = a + h

    while x < b:
        list_x.append(round(x, 4))
        y = fun(list_x[-1], list_y[-1], c)
        x = x + h
        list_y.append(y)

    return list_x, list_y
def milne(f, epsilon, a, y_a, b):
    func = get_function(f)
    # Определяем начальный шаг сетки h
    h = 0.1

    # Находим первые 4 точки методом Рунге-Кутты 4 порядка
    y = [y_a]
    x = [a]
    for i in range(3):
        k1 = func(x[i], y[i])
        k2 = func(x[i] + h / 2, y[i] + h / 2 * k1)
        k3 = func(x[i] + h / 2, y[i] + h / 2 * k2)
        k4 = func(x[i] + h, y[i] + h * k3)
        y.append(y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
        x.append(round((x[i] + h), 5))

    while round((x[-1] + h), 5) <= b:
        # Вычисляем следующую точку
        new_x = round((x[-1] + h), 5)
        y_predicted = y[-4] + 4 * h * (2 * func(x[-1], y[-1]) - func(x[-2], y[-2]) + 2 * func(x[-3], y[-3])) / 3
        while True:
            new_f = func(new_x, y_predicted)
            y_corrected = y[-2] + h * (func(x[-2], y[-2]) + 4 * func(x[-1], y[-1]) + new_f) / 3
            if abs(y_corrected - y_predicted) > epsilon:
                y_predicted = y_corrected
            else:
                break
        x.append(new_x)
        y.append(y_corrected)
    plt.plot(x, y, label='Численное решение')
    plt.plot(x[0], y[0], 'ro', label='Начальная точка')
    x_a, y_a = analytical(f, y_a, a, b)
    plt.plot(x_a, y_a, label='Аналитическое решение')
    # Строим график аналитического решения, если оно задано

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    return y[-1]





if __name__ == '__main__':
    print('1) y\' = sin(x)')
    print('2) y\' = (x * y) / 2')
    print('3) y\' = x - y + 3')
    f = int(input("Введите номер функции:").strip())
    if get_function(f) == 0:
        print("Error")
    else:
        epsilon = float(input("Введите точность:").strip())
        a = float(input("Введите начальное значение x:").strip())
        y_a = float(input("Введите начальное значение y:").strip())
        b = float(input("Введите конечное значение x:").strip())
        result = milne(f, epsilon, a, y_a, b)
        print("Значение y(b):")
        print(str(result) + '\n')
