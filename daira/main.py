import shooting_method
import equations
import graph_drawer

equations.print_equations()
n = int(input())
a = float(input("a: "))
ya = float(input("f(a): "))
b = float(input("b: "))
yb = float(input("f(b): "))
eps = float(input("Eps: "))

y = shooting_method.solve(n, a, ya, b, yb, eps)
graph_drawer.draw(a, b, y, n)
