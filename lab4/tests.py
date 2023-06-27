def get_function_dot(number):
    if number == 1:
        return [[7], [-3, -2, -1, 0, 1, 2, 3], [-3, -2, -1, 0, 1, 2, 3]]  # y = x
    elif number == 2:
        return [[7], [-3, -2, -1, 0, 1, 2, 3], [9, 4, 1, 0, 1, 4, 9]]    # y = x**2
    elif number == 3:   # y = x**2 with loud. Such a bad influence - just 1 incorrect element
        return [[11], [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [25, 16, 11, 4, 1, 0, 1, 6, 9, 16, 25]]
    else:
        return 0
