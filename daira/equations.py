from math import exp, cosh

def print_equations():
    print("""
        1. y'' - y = x 
        2. y'' = x
        3. y'' - y = 0
        4. y'' - 2y' + y = 0
        """)

def get_analytic(n, x):
    match n:
        case 1:
            return exp(x)-exp(-x)-x
        case 2:
            return x + (x**3)/6
        case 3:
            return cosh(x)/cosh(1)
        case 4:
            return x*exp(x)
        case _:
            pass
