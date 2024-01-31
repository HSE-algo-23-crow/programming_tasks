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
    проектами, обеспечивающими максимальную прибыль.
    """
    validate_profit_matrix(profit_matrix)

    n = len(profit_matrix[0])  # number of projects
    m = len(profit_matrix)  # number of investment levels

    # Initialize the dp and paths lists
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    paths = [[[[] for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

    # Fill the dp and paths lists
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(j + 1):
                if k > 0:
                    new_profit = profit_matrix[k - 1][i - 1] + dp[i - 1][j - k]
                    if new_profit > dp[i][j]:
                        dp[i][j] = new_profit
                        paths[i][j] = [path + [k] for path in paths[i - 1][j - k]]
                    elif new_profit == dp[i][j]:
                        paths[i][j] += [path + [k] for path in paths[i - 1][j - k]]
                else:
                    #add zero investment to paths and dp
                    paths[i][j] = [[0] + path for path in paths[i - 1][j]]
                    dp[i][j] = dp[i - 1][j]
            print(paths[1::])

    #remove duplicates
    paths[n][m] = list(set(tuple(path) for path in paths[n][m]))

    i = 0
    while i < len(paths[n][m]):
        if sum(paths[n][m][i]) != m or len(paths[n][m][i]) != n:
            paths[n][m].pop(i)
        else:
            i+=1

    # Return the maximum profit and the corresponding distributions of investments
    return {PROFIT: dp[n][m], DISTRIBUTIONS: paths[n][m]}


def validate_profit_matrix(profit_matrix):
    if not isinstance(profit_matrix, list) or not all(isinstance(row, list) and all(isinstance(value, int) for value in row) for row in profit_matrix):
        raise ValueError(PARAM_ERR_MSG)
    for column in range(1, len(profit_matrix)):
        if len(profit_matrix[column]) != len(profit_matrix[0]):
            raise ValueError(PARAM_ERR_MSG)
    for column in range(len(profit_matrix) - 1):
        for line in range(len(profit_matrix[0])):
            if profit_matrix[column][line] > profit_matrix[column + 1][line]:
                raise ProfitValueError(DECR_PROFIT_ERR_MSG, line, column + 1)

    for column in range(len(profit_matrix)):
        for line in range(len(profit_matrix[0])):
            if profit_matrix[column][line] < 0:
                raise ProfitValueError(NEG_PROFIT_ERR_MSG, line, column)


def main():
    profit_matrix = [[5, 7, 2, 10],
                  [9, 8, 4, 15],
                  [11, 10, 5, 16],
                  [12, 12, 8, 17],
                  [14, 15, 9, 18]]
    print(get_invest_distributions(profit_matrix))


if __name__ == '__main__':
    main()
