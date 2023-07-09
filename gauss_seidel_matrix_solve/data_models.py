import random


class Matrix:
    @staticmethod
    def create_matrix_from_data(
        matrix_init: list[list[int]] = None, answer_list: list = None
    ) -> tuple[list[list[int]], list[int]]:
        A, B = [], []  # noqa
        if matrix_init is None and answer_list is None:
            amount_size_default = 20
            Matrix.create_random_square_matrix(amount_size_default)
        elif matrix_init is not None and answer_list is not None:
            A, B = matrix_init, answer_list  # noqa
        else:
            raise IOError("Please put matrix and solution data to create a matrix")

        Matrix.__matrix_is_valid(matrix=A)
        return A, B

    @staticmethod
    def create_random_square_matrix(
        matrix_size: int = 20, max_value: int = 10
    ) -> tuple[list[list[int]], list[int]]:
        """Generate random matrix in diapason [-max_value; +max_value]
        :param matrix_size: Matrix size
        :type matrix_size: int
        :param max_value: Max absolute value for diapason
        :type max_value: int
        :return: Generate random matrix with size 20*20
        """
        A, B = [], []  # noqa
        # Fill matrix (A) with data
        for _ in range(matrix_size):
            A.append(
                [random.randint(-max_value, max_value) for _ in range(matrix_size)]
            )

        # Make diagonal dominance
        for i in range(matrix_size):
            A[i][i] = sum(map(abs, A[i])) + 1

        # Fill answer (B) with data
        beautiful_answer_coefficient = 100
        for _ in range(matrix_size):
            B.append(
                random.randint(
                    -beautiful_answer_coefficient * max_value,
                    beautiful_answer_coefficient * max_value,
                )
            )
        return A, B

    @staticmethod
    def __matrix_is_valid(matrix) -> None:  # noqa
        """Check if matrix is valid"""
        if len(matrix) == 0:
            raise IOError("Matrix is empty")

        strokes_amount = len(matrix)
        column_amount = len(matrix[0])
        for i in range(strokes_amount):
            if column_amount != len(matrix[i]):
                raise IOError("There are different count of elements in strokes!")
