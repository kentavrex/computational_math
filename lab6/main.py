from lab6 import tests
from lab6.solution import Solution

if __name__ == '__main__':
    print(tests.get_equations())
    f_num = 1
    a = float(input("Enter a: "))
    ya = float(input("Enter y(a): "))
    b = float(input("Enter b: "))
    yb = float(input("Enter y(b): "))
    eps = float(input("Enter eps: "))

    y_numerical = Solution.shooting_method(f_num=f_num, a=a, ya=ya, b=b, yb=yb, eps=eps)
    Solution.draw(a=a, b=b, y_numerical=y_numerical, f_num=f_num, ya=ya, yb=yb)

