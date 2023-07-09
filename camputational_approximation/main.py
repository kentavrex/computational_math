from camputational_approximation.solution import Solution
from camputational_approximation.tests import get_function_dot

if __name__ == '__main__':
    while True:
        var = str(input("Do you want to enter the data automatically from tests [auto/man]: "))
        if var == "man":
            axis_count = int(input("Enter the number of nodes: ").strip())
            print("Enter the starting points: ")
            x_axis = list(map(float, input("x: ").rstrip().split()))
            y_axis = list(map(float, input("y: ").rstrip().split()))
            x = float(input("Enter the point you want to find: ").strip())
            result = Solution.interpolate_by_lagrange(x_axis, y_axis, x)
            print(str(result))
            Solution.plot_interpolate(x_axis, y_axis, x, result)
            break
        elif var == "auto":
            try:
                tests = "1) [[7], [-3, -2, -1, 0, 1, 2, 3], [-3, -2, -1, 0, 1, 2, 3]]  # y = x\n" \
                        "2) [[7], [-3, -2, -1, 0, 1, 2, 3], [9, 4, 1, 0, 1, 4, 9]]    # y = x**2\n" \
                        "3) [[11], [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [25, 16, 11, 4, 1, 0, 1, 6, 9, 16, 25]] incorrect"
                print(tests)
                number = int(input("Enter the test data number: "))
            except:
                continue
            data = get_function_dot(number)
            if data == 0 or isinstance(data, int):
                print("Error")
            else:

                axis_count = data[0][0]
                x_axis = data[1]
                y_axis = data[2]
                x = float(input("Enter the point you want to find: ").strip())
                result = Solution.interpolate_by_lagrange(x_axis, y_axis, x)
                print(str(result))
                Solution.plot_interpolate(x_axis, y_axis, x, result)
                break
        else:
            print("Error")

