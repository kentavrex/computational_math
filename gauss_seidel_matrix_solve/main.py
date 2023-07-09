from loguru import logger

from data_models import Matrix
from solution import Solution


cozy_matrix = Matrix.create_matrix_from_data(
    matrix_init=[
        [11, 4, 4, 1],
        [7, 23, 5, -1],
        [-1, -7, -20, -1],
        [8, -2, -1, -23],
    ],
    answer_list=[19, 34, -29, -18],
)  # root list is: [1, 1, 1, 1]


def realize_gauss_seidel_solution(
    matrix: tuple[list[list[int]], list[int]] = None
) -> None:
    """Realization of Gauss Seidel Method of matrix solving
    :param matrix: Matrix object
    :type matrix: Matrix
    :return: Nothing
    :rtype: None
    """
    solution = Solution(input_data=matrix, eps=1e-7)
    if not solution.check_input_square_matrix():
        return

    root_list, fault_list = solution.solve_matrix()

    format_list = solution.format_list_to_string(
        root_list=root_list, fault_list=fault_list, accuracy=5
    )
    logger.info(format_list)

    solution.check_solution(root_list=root_list)


if __name__ == "__main__":
    # realize_gauss_seidel_solution()
    realize_gauss_seidel_solution(matrix=cozy_matrix)
