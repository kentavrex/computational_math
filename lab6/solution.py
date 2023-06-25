import math

from lab6.tests import get_function, first_function_derivative_2


class Solution:
    @staticmethod
    def newton_method(f, df, x0, eps):
        """Ищет решение f(x)=0 методом Ньютона (метод касательных для решения нелинейных уравнений)

        f - функция от x, для которой ищем решение
        df - производная по x от f
        x0 - начальная точка
        eps - погрешность

        returns:
        x, для которого abs(f(x)) < eps
        """

        while True:
            delta = abs(f(x0))
            if delta < eps:
                return x0
            x0 = x0 - f(x0) / df(x0)

    @staticmethod
    def shoot(fun_y2, y0, ksi, x0=0.0, x1=1.0, n=1000):
        """Рассчитывает один "выстрел" по методу стрельбы

        fun_y2 - вторая производная функции y
        y0 - y(x0)
        ksi - "угол выстрела", т.е. наклон касательной к y, т.е. y(x0)
        x0, x1 - диапазон x, на котором производится расчет
        n - количество блоков, на котороые разбивается диапазон (x0, x1) для расчета

        returns:
        конечное значение пули после выстрела, т.е. y(x1)

        """
        x = x0
        y = y0
        y1 = ksi

        step = (x1 - x0) / n
        for i in range(n):
            x += step
            y += step * y1
            y1 += step * fun_y2(x, y, y1)
        return y

    @staticmethod
    def shooting_method(f, x0, x1, c1, c2, eps=1e-3):
        """Поиск решение ОДУ методом стрельбы

        fun_ode(x,y,y1) - p(x), в выражении если y''=p(x,y,y')
        (x0,y0) - начальная точка
        (x1,y1) - конечная точка
        1e-3 - погрешность

        return:
        угол стрельбы, y'(x0)
        """
        func = get_function(f)
        func_derivative_2 = first_function_derivative_2
        y0 = func(x0, c1=c1, c2=c2)
        y1 = func(x1, c1=c1, c2=c2)

        def F(ksi):
            return Solution.shoot(func_derivative_2, y0, ksi, x0, x1) - y1

        def dF(ksi):
            return F(ksi + eps) - F(ksi) / eps

        return Solution.newton_method(F, dF, x0, eps)
