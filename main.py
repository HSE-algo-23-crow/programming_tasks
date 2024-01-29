import copy
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

def __get_max_profit_by_two_projects(project_matrix, destribution_table, current_index = 1):
    new_destribution_table = [[0 for _ in range(len(destribution_table[0]))] for _ in range(len(project_matrix))]
    profit_table = [0 for _ in range(len(project_matrix))]
    for level in range(1,len(project_matrix) + 1):
        for j in range(0,level + 1):
            if (profit_table[level-1] < ((project_matrix[j - 1][0] if j > 0 else 0)  + (project_matrix[ level - j - 1][1] if j < level else 0))):
                profit_table[level-1] = (project_matrix[j - 1][0] if j > 0 else 0)  + (project_matrix[ level - j - 1][1] if j < level else 0)
                if (j == level):
                    new_destribution_table[level - 1] = destribution_table[level - 1].copy()
                elif (j == 0):
                    new_destribution_table[level-1] = [0 for _ in range(len(destribution_table[0]))]
                    new_destribution_table[level-1][current_index] = level
                else:
                    new_destribution_table[level-1] =destribution_table[ j - 1].copy() if  j - 1  >= 0 else [0 for _ in range(len(destribution_table[0]))]
                    if (current_index == 1):
                        new_destribution_table[level -1][0] = j
                    new_destribution_table[level-1][current_index] = level - j




    return [profit_table,new_destribution_table]

def __check_matrix(matrix):
    if matrix is None or not(len(matrix)):
        raise ValueError(PARAM_ERR_MSG)
    row_len = len(matrix[0])
    if (row_len):
        for row_ind in range(len(matrix)):
            row = matrix[row_ind]
            if (len(row) != row_len):
                raise ValueError(PARAM_ERR_MSG)
            for col_ind in range(len(row)):
                element = row[col_ind]
                if not(type(element) == int):
                    raise ValueError(PARAM_ERR_MSG)
                if (element < 0):
                    raise ProfitValueError(NEG_PROFIT_ERR_MSG,col_ind,row_ind)
                if row_ind > 0:
                    prev_element = matrix[row_ind-1][col_ind]
                    if (prev_element > element):
                        raise ProfitValueError(DECR_PROFIT_ERR_MSG,col_ind,row_ind )
    else:
        raise ValueError(PARAM_ERR_MSG)


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
    __check_matrix(profit_matrix)

    if (len(profit_matrix[0]) == 1):
        return {
            PROFIT: profit_matrix[-1][0],
            DISTRIBUTION: [len(profit_matrix)]
        }
    destribution_table = [[0 for _ in range(len(profit_matrix[0]))] for _ in range(len(profit_matrix))]
    profit_table = []
    current_project = 1
    profit_matrix = copy.deepcopy(profit_matrix)
    while len(profit_matrix[0]) != 1:
        new_table = []
        for i in range(len(profit_matrix)):
            table_row = []
            table_row.append(profit_table[i] if len(profit_table)  else profit_matrix[i][0] )
            table_row.append(profit_matrix[i][1])
            new_table.append(table_row)
        result = __get_max_profit_by_two_projects(new_table,destribution_table,current_project)
        profit_table = result[0]
        destribution_table = result[1]
        current_project +=1
        for i in range(len(profit_matrix)):
            profit_matrix[i].pop(0)
            profit_matrix[i].pop(0)
            profit_matrix[i].insert(0,profit_table[i])
    result = {
        PROFIT: profit_table[-1],
        DISTRIBUTION: destribution_table[-1]
    }
    return result


def main():
    profit_matrix = [[15, 18, 16, 17],
                     [20, 22, 23, 19],
                     [26, 28, 27, 25],
                     [34, 33, 29, 31],
                     [40, 39, 41, 37]]
    print(get_invest_distribution(profit_matrix))


if __name__ == '__main__':
    main()
