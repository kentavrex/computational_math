from lab4.solution import Solution
from lab4.tests import get_function_dot

if __name__ == '__main__':
    var = str(input("Do you want to enter the data manually [y/n]:"))
    if var == "y":
        axis_count = int(input("Enter the number of nodes:").strip())

        print("Enter the starting points")

        x_axis = list(map(float, input("x:").rstrip().split()))

        y_axis = list(map(float, input("y:").rstrip().split()))

        x = float(input("Enter the point you want to find:").strip())

        result = Solution.interpolate_by_lagrange(x_axis, y_axis, x)

        print(str(result) + '\n')

        Solution.plot_interpolate(x_axis, y_axis, x, result)
    elif var == "n":
        number = int(input("Enter the test data number:"))

        data = get_function_dot(number)

        if data == 0:
            print("Error")
        else:
            axis_count = data[0][0]

            x_axis = data[1]

            y_axis = data[2]

            x = float(input("Enter the point you want to find:").strip())

            result = Solution.interpolate_by_lagrange(x_axis, y_axis, x)

            print(str(result) + '\n')

            Solution.plot_interpolate(x_axis, y_axis, x, result)
    else:
        print("Error")

