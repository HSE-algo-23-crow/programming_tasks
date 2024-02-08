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
    check_validation(profit_matrix)
    max_profit_matrix = get_max_profit(profit_matrix)
    profit = max_profit_matrix[-1][-1]
    distribution = get_distribution(max_profit_matrix, profit_matrix)

    return {PROFIT: profit, DISTRIBUTION: distribution}

def check_validation(profit_matrix: list[list[int]]):
    if profit_matrix is None or profit_matrix == [] or profit_matrix == [[]]:
        raise ValueError(PARAM_ERR_MSG)

    if not profit_matrix:
        raise ValueError(PARAM_ERR_MSG)

    if profit_matrix == [[]]:
        raise ValueError(PARAM_ERR_MSG)

    first_row_len = len(profit_matrix[0])
    for row in profit_matrix:
        # Проверка на то, что в матрице нет строк разной длины
        if len(row) != first_row_len:
            raise ValueError(PARAM_ERR_MSG)
        for item in row:
            # Проверка на то, что в матрице только тип float и int
            if not isinstance(item, int) and not isinstance(item, float):
                raise ValueError(PARAM_ERR_MSG)
        for item in row:
            # Проверка на то, что в матрице нет отрицательных значений
            if item < 0:
                raise ProfitValueError(NEG_PROFIT_ERR_MSG, row.index(item), profit_matrix.index(row))
    for proj_index in range (len(profit_matrix[0])):
        for row in range (len(profit_matrix)-1):
            if profit_matrix[row+1][proj_index] < profit_matrix[row][proj_index]:
                raise ProfitValueError(DECR_PROFIT_ERR_MSG, proj_index, row + 1)
def get_max_profit(profit_matrix):
    dynamic_profit_matrix = [[*row] for row in profit_matrix]
    for proj_col_idx in range(len(dynamic_profit_matrix[0]) - 1):
        profit_list = []  # вспомогательный список для хранения максимальных значений прибыли
        for project_row_idx in range(len(dynamic_profit_matrix)):
            max_profit = 0
            for start_idx in range(project_row_idx + 2):
                end_idx = project_row_idx - start_idx + 1

                if start_idx == 0:
                    all_in_last = dynamic_profit_matrix[end_idx - 1][proj_col_idx + 1]
                    max_profit = max(max_profit, all_in_last)
                    continue

                if end_idx == 0:
                    all_in_first = dynamic_profit_matrix[start_idx - 1][proj_col_idx]
                    max_profit = max(max_profit, all_in_first)
                    continue
                different_distribution = dynamic_profit_matrix[start_idx - 1][proj_col_idx] + dynamic_profit_matrix[end_idx - 1][proj_col_idx + 1]
                max_profit = max(different_distribution, max_profit)

            profit_list.append(max_profit)

        for i in range(len(profit_list)):
            dynamic_profit_matrix[i][proj_col_idx + 1] = profit_list[i] # со второго столбца записываем макс прибыль

    extended_matrix = [[0] * len(dynamic_profit_matrix[0])] + dynamic_profit_matrix
    extended_matrix = [[0] + row for row in extended_matrix]

    return extended_matrix

def get_distribution(max_profit_matrix, profit_matrix):
    distribution = [0] * len(profit_matrix[0])
    target_profit = max_profit_matrix[-1][-1]
    ex_proj_cnt = len(max_profit_matrix[0])
    level_cnt = len(max_profit_matrix) - 1
    for proj_idx in range(ex_proj_cnt - 1, 0, -1):
        target_level = level_cnt - sum(distribution)
        for prev_level in range(target_level + 1):
            cur_level = target_level - prev_level
            prev_profit = max_profit_matrix[prev_level][proj_idx - 1]
            cur_profit = 0 if cur_level == 0 else profit_matrix[cur_level-1][proj_idx - 1]
            if cur_profit + prev_profit >= target_profit:
                distribution[proj_idx - 1] = cur_level
                target_profit -= cur_profit
                break
    return distribution

def main():
    profit_matrix = [[1, 2, 2],
                  [3, 5, 4],
                  [7, 6, 5]]
    print(get_invest_distribution(profit_matrix))


if __name__ == '__main__':
    main()
