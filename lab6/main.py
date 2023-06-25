from lab6.solution import Solution
from lab6.tests import first_function_derivative

if __name__ == '__main__':
    funcs = '1) x ** 6 / 30 + c1 * x + c2'
    print(funcs)
    f = int(input("Func number: ").strip())

    # Для любых c1 и c2 не должен срабатывать assert
    c1 = 1
    c2 = 1
    print("c1=", c1)
    print("c2=", c2)

    x0 = 0.0
    x1 = 1.0

    calculated_ksi = Solution.shooting_method(f=f, x0=x0, x1=x1, c1=c1, c2=c2)

    ksi = first_function_derivative(x0, c1)

    print("ksi=", ksi)
    print("расчетный ksi=", calculated_ksi)
    assert abs(calculated_ksi - ksi) < 1e-3, "разница должна быть мала для любых c1 и c2"

    # c1= 1
    # c2= 1
    # ksi= 1.0
    # расчетный ksi= 0.9999925196666988
