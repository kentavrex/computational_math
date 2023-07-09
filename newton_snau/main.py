from typing import Callable

from solution import Solution


class Examples:
    """Class for examples show for all realized methods"""

    @staticmethod
    def chord_method_example():
        """Chord method realization"""
        eps = 0.002
        f: Callable[[float], float] = lambda x: x**3 - 0.2 * x**3 - 0.2 * x - 1.2
        interval: tuple[float, float] = (1, 1.5)
        print(Solution.chord_method(func=f, segment=interval, eps=eps))

    @staticmethod
    def tangent_method_example():
        """Tangent method realization"""
        eps = 0.01
        f: Callable[[float], float] = lambda x: x**3 - 0.2 * x**3 - 0.2 * x - 1.2
        interval: tuple[float, float] = (1, 2)
        print(Solution.tangent_method(func=f, segment=interval, eps=eps))

    @staticmethod
    def newton_method_example():
        """Newton method realization of non-linear system"""
        systems = [
            "1) sin(x); x*y/2",
            "2) tan(x*y+0.4)-x²; 0.9*x²+2*y²-1",
            "3) tan(x*y)-x²; 0.5*x²+2*y²-1",
            "4) x²+y²+z²-1; 2*x²+y²-4*z; 3*x²-4*y+z²"
        ]
        print("\n".join(systems))
        system_id = int(input("Enter system number: ").strip())
        number_of_unknowns = int(input("Enter unknown vars numbers: ").strip())
        initial_approximations = []

        for i in range(number_of_unknowns):
            initial_approximations_item = float(
                input(f"Enter approximation {i+1}: ").strip()
            )
            initial_approximations.append(initial_approximations_item)

        result = Solution.solve_by_fixed_point_iterations(
            system_id=system_id,
            number_of_unknowns=number_of_unknowns,
            initial_approximations=initial_approximations,
        )
        print(result)


if __name__ == "__main__":
    Examples.chord_method_example()
    Examples.tangent_method_example()
    # Examples.newton_method_example()
