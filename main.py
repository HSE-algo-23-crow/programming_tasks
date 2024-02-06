PROFIT = 'profit'
DISTRIBUTION = 'distribution'
PARAM_ERR_MSG = ('Таблица прибыли от проектов не является прямоугольной '
                 'матрицей с числовыми значениями')
NEG_PROFIT_ERR_MSG = 'Значение прибыли не может быть отрицательно'
DECR_PROFIT_ERR_MSG = 'Значение прибыли не может убывать с ростом инвестиций'


class ProfitValueError(Exception):
    def __init__(self, message, project_idx, row_idx):
        self.project_idx = project_idx
        self.row_idx = row_idx
        super().__init__(message)


def get_invest_distribution(profit_matrix: list[list[int]]) -> \
        dict[str: int, str: list[int]]:
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
    distribution - распределение инвестиций между проектами.
    """
    if (not profit_matrix) or (not isinstance(profit_matrix,list) or (profit_matrix is None) or (profit_matrix == []) or (profit_matrix == [[]])):
        raise ValueError(PARAM_ERR_MSG)

    first_row_length = len(profit_matrix[0])
    for row_index, row in enumerate(profit_matrix):
        if len(row) != first_row_length:
            raise ValueError(PARAM_ERR_MSG)

        for item in row:
            if not isinstance(item, (int, float)):
                raise ValueError(PARAM_ERR_MSG)

        for col_index, item in enumerate(row):
            if item < 0:
                raise ProfitValueError(NEG_PROFIT_ERR_MSG, col_index, row_index)
            if row_index > 0 and profit_matrix[row_index - 1][col_index] > item:
                raise ProfitValueError(DECR_PROFIT_ERR_MSG, col_index, row_index)


    num_projects = len(profit_matrix[0])
    num_levels = len(profit_matrix)

    if num_projects == 0 or num_levels == 0:
        return {PROFIT: 0, DISTRIBUTION: [0] * num_projects}


    for project_index in range(num_projects):
        for level_index in range(num_levels):
            if profit_matrix[level_index][project_index] < 0:
                raise ProfitValueError(NEG_PROFIT_ERR_MSG, level_index, project_index)
            if level_index > 0 and profit_matrix[level_index][project_index] < profit_matrix[level_index - 1][project_index]:
                raise ProfitValueError(DECR_PROFIT_ERR_MSG, level_index, project_index)
    max_profit_table = [[0]*(num_projects+1) for _ in range(num_levels+1)]
    distribution_table = [[0] * (num_projects + 1) for _ in range(num_levels + 1)]

    for project_index in range(1, num_projects+1):
        for level_index in range(1, num_levels+1):
            for prev_level in range (level_index+1):
                current_level = level_index-prev_level
                prev_profit = max_profit_table[prev_level][project_index-1]
                current_profit = 0 if current_level == 0 else profit_matrix [current_level-1][project_index-1]
                if (prev_profit+current_profit > max_profit_table[level_index][project_index]):
                    max_profit_table[level_index][project_index] = prev_profit+current_profit
                    distribution_table[level_index][project_index] = current_level
    distribution = [0] * num_projects
    for project_index in range (num_projects,0,-1):
        target_level = num_levels - sum(distribution)
        distribution[project_index-1] = distribution_table[target_level][project_index]

    return {PROFIT: max_profit_table [-1][-1], DISTRIBUTION:distribution }
def main():
    profit_matrix = [[15, 18, 16, 17],
                     [20, 22, 23, 19],
                     [26, 28, 27, 25],
                     [34, 33, 29, 31],
                     [40, 39, 41, 37]]
    print(get_invest_distribution(profit_matrix))


if __name__ == '__main__':
    main()
