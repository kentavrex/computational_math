from typing import Callable


def get_equations():
    equations = "y'' - 5 = 0"
    return equations

def get_analytical_solve(f_num, x, ya, yb, a, b) -> float:
    match f_num:
        case 1:
            c1 = (ya - yb - 5/2*(a**2 - b**2)) / (a-b)
            c2 = ya - 5/2*a**2 - c1*a
            return 5/2 * (x**2) + c1*x + c2
        case _:
            pass

class PQF:
    class PQF1:
        @staticmethod
        def p(x):
            return 0

        @staticmethod
        def q(x):
            return 0

        @staticmethod
        def f(x):
            return 5


def get_pqf(f_num) -> tuple[Callable, Callable, Callable]:
    p, q, f = None, None, None
    match f_num:
        case 1:
            p, q, f = PQF.PQF1.p, PQF.PQF1.q, PQF.PQF1.f
    return p, q, f