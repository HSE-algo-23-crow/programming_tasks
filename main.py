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

    (max_profit, paths) = get_max_profit(profit_matrix)

    return {PROFIT: max_profit, DISTRIBUTIONS: paths}


def get_max_profit(profit_matrix: list[list[int]]) -> tuple[int, list[list[int]]]:
    project_count = len(profit_matrix[0])
    level_count = len(profit_matrix)

    max_profits: dict[int, int] = {
        0: 0
    }
    max_profit_paths: dict[int, list[list[int]]] = {
        0: [[0]]
    }

    # Делаем таблицу с прибылью для первого проекта в качестве первоначальной оптимальной таблицы
    for init_profit in range(1, level_count + 1):
        max_profits[init_profit] = profit_matrix[init_profit - 1][0]
        max_profit_paths[init_profit] = [[init_profit]]

    for project_index in range(1, project_count):
        # Делаем копии, чтобы в моменте подсчета вариантов распределения инвестиций для двух проектов не было
        # уже заменных значений, во избежании ошибок
        copy_max_profits = max_profits.copy()
        copy_max_profit_paths = copy.deepcopy(max_profit_paths)
        for level_index in range(1, level_count + 1):
            for profit in range(1, level_index + 1):
                target_profit = level_index - profit # Ищем какой уровень нам нужно взять из оптимальной таблицы
                current_profit = copy_max_profits[target_profit] + profit_matrix[profit - 1][project_index]

                if current_profit > max_profits[level_index]:
                    # Если мы нашли профит больше, чем текущий, то заменяем его
                    max_profits[level_index] = current_profit
                    max_profit_paths[level_index].clear()
                    # Очищаем старый путь и записываем новые пути к нему
                    for path in copy_max_profit_paths[target_profit]:
                        max_profit_paths[level_index].append([*path[:], profit])

                elif current_profit == max_profits[level_index]:
                    for path in copy_max_profit_paths[target_profit]:
                        max_profit_paths[level_index].append([*path[:], profit])
        for (key, paths) in max_profit_paths.items():
            for path in paths:
                # Добавляем нули в пути, если они оптимальные, но были добавлены в прошлой итерации и не были удалены
                if len(path) < project_index + 1:
                    path.append(0)


        max_profit_paths[0][0].append(0)



    return tuple([max_profits[len(profit_matrix)], max_profit_paths[level_count]])



def validate_profit_matrix(profit_matrix: list[list[int]]) -> None:
    """
    Валидация входной матрицы прибыли
    :param profit_matrix: матрица с прибылями
    """
    if profit_matrix is None or len(profit_matrix) == 0 or len(profit_matrix[0]) == 0:
        raise ValueError(PARAM_ERR_MSG)
    max_length = max(map(len, profit_matrix))
    for level_index, row in enumerate(profit_matrix):
        if max_length != len(row):
            raise ValueError(PARAM_ERR_MSG)

        for project_index, num in enumerate(row):
            if level_index != 0:
                if profit_matrix[level_index - 1][project_index] > num:
                    raise ProfitValueError(DECR_PROFIT_ERR_MSG, project_index, level_index)
            if not isinstance(num, int):
                raise ValueError(PARAM_ERR_MSG)
            if num < 0:
                raise ProfitValueError(NEG_PROFIT_ERR_MSG, project_index, level_index)





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
