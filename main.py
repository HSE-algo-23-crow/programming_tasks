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

def __get_max_profit_matrix(profit_matrix):
    num_rows = len(profit_matrix)
    num_cols = len(profit_matrix[0])
    max_profit_matrix = [[0] * (num_rows + 1) for _ in range(num_cols + 1)]

    for col in range(1, num_cols + 1):
        for row in range(1, num_rows + 1):
            max_profit = 0
            for k in range(row + 1):
                profit = profit_matrix[k - 1][col - 1] if k > 0 else 0
                max_profit = max(max_profit, profit + max_profit_matrix[col - 1][row - k])
            max_profit_matrix[col][row] = max_profit

    return max_profit_matrix

def __get_distribution(max_profit_matrix, profit_matrix):
    num_rows = len(profit_matrix)
    num_cols = len(profit_matrix[0])
    distribution = [0] * num_cols
    total_investment = num_rows

    for col in range(num_cols, 0, -1):
        for row in range(total_investment + 1):
            if max_profit_matrix[col][total_investment] == max_profit_matrix[col - 1][row] + (profit_matrix[total_investment - row - 1][col - 1] if total_investment - row > 0 else 0):
                distribution[col - 1] = total_investment - row
                total_investment = row
                break

    return distribution
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
    __validate_matrix(profit_matrix)
    max_profit_matrix = __get_max_profit_matrix(profit_matrix)
    distribution = __get_distribution(max_profit_matrix, profit_matrix)
    return {PROFIT: max_profit_matrix[-1][-1], DISTRIBUTION: distribution}

def __validate_matrix(profit_matrix):
    if not profit_matrix or not all(profit_matrix):
        raise ValueError(PARAM_ERR_MSG)
    num_rows = len(profit_matrix)
    num_cols = len(profit_matrix[0])
    for i in range(num_rows):
        if len(profit_matrix[i]) != num_cols:
            raise ValueError(PARAM_ERR_MSG)
        for j in range(num_cols):
            if profit_matrix[i][j] is None or type(profit_matrix[i][j]) not in [int, float]:
                raise ValueError(PARAM_ERR_MSG)
            if profit_matrix[i][j] < 0:
                raise ProfitValueError(NEG_PROFIT_ERR_MSG, j, i)
            if i > 0 and profit_matrix[i][j] < profit_matrix[i-1][j]:
                raise ProfitValueError(DECR_PROFIT_ERR_MSG, j, i)
def main():
    profit_matrix = [[15, 18, 16, 17],
                     [20, 22, 23, 19],
                     [26, 28, 27, 25],
                     [34, 33, 29, 31],
                     [40, 39, 41, 37]]
    print(get_invest_distribution(profit_matrix))


if __name__ == '__main__':
    main()
