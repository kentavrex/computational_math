def solve(f, a, ya, b, yb, eps):
    n = 10
    aa = a
    yaa = ya
    while True:
        a = aa
        ya = yaa
        y1 = (yb - ya) / (b - a)
        h = (b - a) / n
        y = []
        for i in range(n):
            y.append(ya)
            y2 = second_derivative(ya, a, y1, f)
            y1_dx = y1 + y2 * h
            y_dx = ya + (y1 + y1_dx) * h / 2
            y2_dx = (ya + y_dx) / 2 + a + h
            a += h
            ya = ya + (y1 + (y1 + (y2 + y2_dx) * h / 2)) * h / 2
            y1 = y1 + (y2 + y2_dx) * h / 2
            if (y1 > 0):
                if (ya >= yb):
                    break
        if abs(y[-1] - yb) < eps:
            return y
        n *= 10

def second_derivative(ya, a, y1, f):
    match f:
        case 1:
            return ya + a
        case 2:
            return a
        case 3:
            return ya
        case 4:
            return 2*y1+ya
        case _:
            pass
