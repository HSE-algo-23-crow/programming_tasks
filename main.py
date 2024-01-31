from audioop import reverse

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


def check_matrix(profit_matrix: list[list[int]]) -> None:
    if profit_matrix is None:
        raise ValueError(PARAM_ERR_MSG)
    if not profit_matrix:
        raise ValueError(PARAM_ERR_MSG)
    if any(not row for row in profit_matrix):
        raise ValueError(PARAM_ERR_MSG)
    num_cols = len(profit_matrix[0])
    if any(len(row) != num_cols for row in profit_matrix):
        raise ValueError(PARAM_ERR_MSG)
    incorrect_values = [None, 'str', []]
    if any(value in incorrect_values for row in profit_matrix for value in row):
        raise ValueError(PARAM_ERR_MSG)
    for col in range(num_cols):
        for row in range(len(profit_matrix)):
            value = profit_matrix[row][col]
            if value < 0:
                raise ProfitValueError(NEG_PROFIT_ERR_MSG, col, row)
    for col in range(num_cols):
        prev_value = 0
        for row in range(len(profit_matrix)):
            value = profit_matrix[row][col]
            if value < prev_value:
                raise ProfitValueError(DECR_PROFIT_ERR_MSG, col, row)
            prev_value = value


def get_invest_distribution(profit_matrix: list[list[int]]) -> dict[str: int, str: list[int]]:
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
    check_matrix(profit_matrix)
    num_rows = len(profit_matrix)
    num_cols = len(profit_matrix[0])
    max_profit_dict = {}

    for col in range(1, num_cols + 1):
        for row in range(1, num_rows + 1):
            max_profit = 0
            for k in range(row + 1):
                profit = profit_matrix[k - 1][col - 1] if k > 0 else 0
                max_profit = max(max_profit, profit + max_profit_dict.get((col - 1, row - k), 0))
            max_profit_dict[(col, row)] = max_profit

    max_profit = max_profit_dict[(num_cols, num_rows)]

    distribution = []

    def backtrack(col, row):
        if col == 0:
            return
        optimal_k = 0
        optimal_profit = 0
        for k in range(row + 1):
            profit = profit_matrix[k - 1][col - 1] if k > 0 else 0
            profit += max_profit_dict.get((col - 1, row - k), 0)
            if profit > optimal_profit:
                optimal_profit = profit
                optimal_k = k
        distribution.append(optimal_k)
        backtrack(col - 1, row - optimal_k)

    backtrack(num_cols, num_rows)
    distribution.reverse()

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
