import copy

PROFIT = 'profit'
DISTRIBUTIONS = 'distributions'
PARAM_ERR_MSG = ('Таблица прибыли от проектов не является прямоугольной '
                 'матрицей с числовыми значениями')
NEG_PROFIT_ERR_MSG = 'Значение прибыли не может быть отрицательно'
DECR_PROFIT_ERR_MSG = 'Значение прибыли не может убывать с ростом инвестиций'


class ProfitValueError(Exception):
    def __init__(self, message, project_idx, row_idx):
        self.project_idx = project_idx
        self.row_idx = row_idx
        super().__init__(message)


def get_invest_distributions(profit_matrix: list[list[int]]) -> \
        dict[str: int, str: list[list[int]]]:

    """Рассчитывает максимально возможную прибыль и распределение инвестиций
    между несколькими проектами. Инвестиции распределяются кратными частями.
    :param profit_matrix: Таблица с распределением прибыли от проектов в
    зависимости от уровня инвестиций. Проекты указаны в столбцах, уровни
    инвестиций в строках.
    :raise ValueError: Если таблица прибыли от проектов не является
    прямоугольной матрицей с числовыми значениями.
    :raise ProfitValueError: Если значение прибыли отрицательно или убывает
    с ростом инвестиций.
    :return: Словарь с ключами:
    profit - максимально возможная прибыль от инвестиций,
    distributions - списком со всеми вариантами распределения инвестиций между
    проектами, обеспечивающими максимальную прибыль
    """

    validate_profit_matrix(profit_matrix)

    max_profit_table = get_max_profit_table(profit_matrix)

    max_profit = max_profit_table[-1][-1]
    distribution = get_distribution(max_profit_table, profit_matrix)
    print(max_profit_table)
    return {PROFIT: max_profit, DISTRIBUTIONS: [distribution]}


def validate_profit_matrix(profit_matrix: list[list[int]]) -> None:
    """
    Валидация входной матрицы прибыли
    :param profit_matrix: матрица с прибылями
    """
    if profit_matrix is None or len(profit_matrix) == 0 or len(profit_matrix[0]) == 0:
        raise ValueError(PARAM_ERR_MSG)
    max_length = max(map(len, profit_matrix))
    for i, row in enumerate(profit_matrix):
        if max_length != len(row):
            raise ValueError(PARAM_ERR_MSG)

        for j, num in enumerate(row):
            if i != 0:
                if profit_matrix[i - 1][j] > num:
                    raise ProfitValueError(DECR_PROFIT_ERR_MSG, j, i)
            if not isinstance(num, int):
                raise ValueError(PARAM_ERR_MSG)
            if num < 0:
                raise ProfitValueError(NEG_PROFIT_ERR_MSG, j, i)


def get_max_profit_table(profit_matrix):
    project_count = len(profit_matrix[0]) + 1
    level_count = len(profit_matrix) + 1

    max_profit_matrix = [ [0] * level_count for i in range(project_count)]

    for project_index in range(1, project_count):

        for level_index in range(1, level_count):
            max_profit = max_profit_matrix[project_index - 1][level_index]

            for prev_level in range(1, level_index + 1):
                another_level = level_index - prev_level
                current_profit = profit_matrix[prev_level - 1][project_index - 1]

                max_profit = max(max_profit, current_profit + max_profit_matrix[project_index - 1][another_level])

            max_profit_matrix[project_index][level_index] = max_profit

    return max_profit_matrix


def get_distribution(max_profit_matrix, profit_matrix):
    project_count = len(profit_matrix[0])
    level_count = len(profit_matrix)
    distribution = [0] * project_count

    target_level = level_count

    for project_index in range(project_count, 0, -1):

        for level_index in range(0, target_level + 1):
            another_level = target_level - level_index - 1
            if max_profit_matrix[project_index][target_level] == max_profit_matrix[project_index - 1][level_index] + profit_matrix[another_level][project_index - 1]:
                distribution[project_index - 1] = another_level + 1
                target_level = level_index
                break

    return distribution


def main():
    # test case
    matrix = [[5, 7, 2, 10],
              [9, 8, 4, 15],
              [11, 10, 5, 16],
              [12, 12, 8, 17],
              [14, 15, 9, 18]]
    print(get_invest_distributions(matrix))


if __name__ == '__main__':
    main()
