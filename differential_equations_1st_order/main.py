from differential_equations_1st_order.solution import Solution

if __name__ == '__main__':
    funcs = '1) y\' = (x / y) * 4\n' \
            '2) y\' = cos(x)\n' \
            '3) y\' = x - y + 7'
    print(funcs)
    f = int(input("Func number: ").strip())
    epsilon = float(input("Epsilon: ").strip())
    a = float(input("x0: ").strip())
    y_a = float(input("y0: ").strip())
    b = float(input("x for point search: ").strip())
    result = Solution.solveByMilne(f, epsilon, a, y_a, b)
    print(f"y(b) value: {result}")
