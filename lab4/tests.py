def get_function_dot(number):
    if number == 1:
        return [[5], [-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]]
    elif number == 2:
        return [[5], [-1, -2, 0, 2, 1], [-1, -2, 0, 2, 1]]
    elif number == 3:
        return [[9], [-4, -3, -2, -1, 0, 1, 2, 3, 4], [16, 11, 4, 1, 0, 1, 6, 9, 16]]
    elif number == 4:
        return [[4], [0, 2, 3, 5], [1, 3, 2, 5]]
    else:
        return 0
