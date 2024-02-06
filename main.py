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


    if not all(isinstance(row, list) for row in profit_matrix) or not profit_matrix:
        raise ValueError(PARAM_ERR_MSG)

    num_projects = len(profit_matrix[0])
    num_levels = len(profit_matrix)

    if num_projects == 0 or num_levels == 0:
        return {PROFIT: 0, DISTRIBUTION: [0] * num_projects}

    max_profit = 0
    distribution = [0] * num_projects

    for i in range(num_levels):
        for j in range(num_projects):
            if profit_matrix[i][j] < 0:
                raise ProfitValueError(NEG_PROFIT_ERR_MSG, j, i)
            if i > 0 and profit_matrix[i][j] < profit_matrix[i - 1][j]:
                raise ProfitValueError(DECR_PROFIT_ERR_MSG, j, i)
            if profit_matrix[i][j] > distribution[j]:
                max_profit += profit_matrix[i][j] - distribution[j]
                distribution[j] = profit_matrix[i][j]

    return {PROFIT: max_profit, DISTRIBUTION: distribution}
def main():
    profit_matrix = [[15, 18, 16, 17],
                     [20, 22, 23, 19],
                     [26, 28, 27, 25],
                     [34, 33, 29, 31],
                     [40, 39, 41, 37]]
    print(get_invest_distribution(profit_matrix))


if __name__ == '__main__':
    main()
