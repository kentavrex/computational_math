from loguru import logger

from data_models import Matrix


class Solution:
    def __init__(
        self, input_data: tuple[list[list[int]], list[int]] = None, eps: float = 1e-6
    ):
        self.eps = eps
        self.A: list[list[int]] = [[]]
        self.B: list[int] = []
        try:
            self.A, self.B = input_data[0], input_data[1]  # From extended matrix
        except TypeError:
            self.A, self.B = Matrix.create_random_square_matrix()

    def solve_matrix(self) -> tuple[list[float], list[float]]:
        """Gauss Seidel Method Realization
        :return: List of matrix's roots and list of faults
        :rtype: tuple[list[float], list[float]]
        """
        num_of_stroke_elements = len(self.A)
        # First approximation
        old_list = [self.B[i] / self.A[i][i] for i in range(num_of_stroke_elements)]
        fault = self.eps + 1
        iteration = 1
        result_list, fault_list = [], []

        while fault > self.eps:
            result_list = []
            for i in range(num_of_stroke_elements):
                main_diagonal_element_coefficient = self.A[i][i]
                # First subtraction: f.e. x1 = (-> b1/5 <-) - x2/5 - ...
                new_value = self.B[i] / main_diagonal_element_coefficient

                for j in range(i):
                    # Other subtractions: f.e. x1 = b1/5 - (-> A_EL* x2/5 <-) - ...,
                    # where A_EL = value in list after THIS approximation == Gauss Seidel Method
                    new_value -= result_list[j] * (
                        self.A[i][j] / main_diagonal_element_coefficient
                    )

                for j in range(i + 1, num_of_stroke_elements):
                    # Other subtractions: f.e. x1 = b1/5 - (-> A_EL* x2/5 <-) - ...,
                    # where A_EL = value in list after PREVIOUS approximation
                    new_value -= old_list[j] * (
                        self.A[i][j] / main_diagonal_element_coefficient
                    )

                result_list.append(new_value)

            fault_list = [
                abs(result_list[i] - old_list[i]) for i in range(num_of_stroke_elements)
            ]
            max_fault_from_iteration = max(fault_list)
            if iteration > 6 and max_fault_from_iteration > fault:
                raise ValueError("Something gone wrong. The fault do not decrease!")

            fault = max_fault_from_iteration

            old_list = result_list[:]
            iteration += 1

        logger.info(f"Success! Amount iterations: {iteration}")

        return result_list, fault_list

    @staticmethod
    def format_list_to_string(
        root_list: list[float] | None, fault_list: list[float] | None, accuracy: int = 5
    ) -> str:
        """Format list data to output string
        :param root_list: List of matrix's roots
        :type root_list: list[float]
        :param fault_list: List of faults
        :type fault_list: list[float]
        :param accuracy: How much numbers after comma to show
        :return: Formatted output
        :rtype: str
        """
        res = ""
        if not root_list:
            logger.error("There is no solution for your matrix")
            return res

        for i in range(len(root_list)):
            res += f"\nx{i + 1}: {round(root_list[i], accuracy)}"
            res += "    "
            res += f"fault: {round(fault_list[i], 12)}"
        return res

    def check_solution(self, root_list: list[float] | None) -> bool:
        """Check if solution is correct. Substitute the calculated values
        into the original equations
        :param root_list: List of matrix's roots
        :type root_list: list[float]
        :return: Result of check
        :rtype: bool
        """
        if not self.A:
            logger.error("Matrix is empty or does not exists")
            return False

        matrix_size = len(self.A)
        for i in range(matrix_size):
            left_part_of_equation, sum_of_faults = 0, 0
            for j in range(matrix_size):
                input_matrix_element = self.A[i][j]
                left_part_of_equation += input_matrix_element * root_list[j]
                sum_of_faults += abs(input_matrix_element) * self.eps

            # Correct if left part of equation places in diapason of right part +- fault
            if not (
                    self.B[i] - sum_of_faults
                    <= left_part_of_equation
                    <= self.B[i] + sum_of_faults
            ):
                logger.error("Solution is incorrect!")
                return False

        logger.info(f"Solution is correct! Your accuracy is {self.eps}")
        return True

    def check_input_square_matrix(self) -> bool:
        """Check matrix is valid for Gauss Seidel Method
        :return: Is matrix valid
        :rtype: bool
        """
        strokes_amount = len(self.A)
        for i in range(strokes_amount):
            if self.A[i][i] == 0:
                logger.error(
                    "Method Gauss Seidel works only with not 0 values in diagonal"
                )
                return False

            # Diagonal element should be more than summ of other elements in line
            if abs(self.A[i][i]) < (sum(map(abs, self.A[i])) - abs(self.A[i][i])):
                logger.error("Diagonal dominance condition is fault")
                return False
        return True
