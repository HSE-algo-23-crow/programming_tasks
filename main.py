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


def sums(length, total_sum):
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in sums(length - 1, total_sum - value):
                yield (value,) + permutation


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

    routes = list(sums(n, m))

    max_sum = 0
    max_routes = []

    for i in routes:
        cur_sum = 0
        cur_route = list(i)
        for j in range(len(cur_route)):
            if cur_route[j] == 0:
                continue
            cur_sum += profit_matrix[cur_route[j]-1][j]

        if cur_sum > max_sum:
            max_sum = cur_sum
            max_routes = [i]
        elif cur_sum == max_sum:
            max_routes.append(i)

    # Return the maximum profit and the corresponding distributions of investments
    return {PROFIT: max_sum, DISTRIBUTIONS: max_routes}


def validate_profit_matrix(profit_matrix):
    if profit_matrix is None or len(profit_matrix) == 0 or not isinstance(profit_matrix, list) or not all(isinstance(row, list) and all(isinstance(value, int) for value in row) for row in profit_matrix):
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

    for i in profit_matrix:
        if len(i) == 0:
            raise ValueError(PARAM_ERR_MSG)


def main():
    profit_matrix = [[5, 7, 2, 10],
                     [9, 8, 4, 15],
                     [11, 10, 5, 16],
                     [12, 12, 8, 17],
                     [14, 15, 9, 18]]
    print(get_invest_distributions(profit_matrix))


if __name__ == '__main__':
    main()
