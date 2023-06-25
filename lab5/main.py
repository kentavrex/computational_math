from vychmat.lab5.solution import Solution

if __name__ == '__main__':
    funcs = '1) y\' = sin(x)\n' \
            '2) y\' = (x * y) / 2\n' \
            '3) y\' = x - y + 3\n'
    print(funcs)
    f = int(input("Func number: ").strip())
    epsilon = float(input("Epsilon: ").strip())
    a = float(input("x0: ").strip())
    y_a = float(input("y0: ").strip())
    b = float(input("x for point search: ").strip())
    result = Solution.solveByMilne(f, epsilon, a, y_a, b)
    print(f"y(b) value: {result}")
