import math

DIF_LEN_EXCEPTION = "Количество строк в матрице отличается от количества столбцов"
ZERO_MATRIX_EXCEPTION = "Матрица не содержит строк"
ERROR_TYPE_EXCEPTION = "Ячейки матрицы должны представлять собой число"
LESS_ZERO = "Вес ребра должен быть >= 0"
NOT_WEIGHTED = "Граф не является взвешенным"
NODE_NOT_CONNECTED_EXCEPTION = "Вершина под номером {0} никак не связана с другими"


# Здесь будет исходный код разработанного алгоритма
def __check_params(matrix: list[list[int]]):
    matr_len = len(matrix)
    if matr_len == 0:
        raise Exception(ZERO_MATRIX_EXCEPTION)
    for i in range(len(matrix)):
        if len(matrix[i]) != matr_len:
            raise Exception(DIF_LEN_EXCEPTION)
        sum = 0
        for j in range(len(matrix[i])):
            x = matrix[i][j]
            if type(x) != int and type(x) != float:
                raise Exception(ERROR_TYPE_EXCEPTION)
            if x < 0:
                raise Exception(LESS_ZERO)
            if x != matrix[j][i]:
                raise Exception(NOT_WEIGHTED)
            sum += x
        if sum == 0:
            raise Exception(NODE_NOT_CONNECTED_EXCEPTION.format(str(i + 1)))


def prim_algorythm(matrix: list[list[int]], first_node_index: int) -> list[list[int]]:
    __check_params(matrix)
    N = len(matrix)
    selected_node = [False if i != first_node_index else True for i in range(N)]
    no_edge = 0
    result = []
    while no_edge < N - 1:
        minimum = math.inf
        a = 0
        b = 0
        for m in range(N):
            if selected_node[m]:
                for n in range(N):
                    if (not selected_node[n]) and matrix[m][n]:
                        # not in selected and there is an edge
                        if minimum > matrix[m][n]:
                            minimum = matrix[m][n]
                            a = m
                            b = n
        result.append([a, b, matrix[a][b]])
        selected_node[b] = True
        no_edge += 1
    return result


def main():
    matrix = [
        [0, 19, 5, 0, 0],
        [19, 0, 5, 9, 2],
        [5, 5, 0, 1, 6],
        [0, 9, 1, 0, 1],
        [0, 2, 6, 1, 0],
    ]
    print("Матрица ребер графа:")
    for row in matrix:
        print(*row)
    result = prim_algorythm(matrix, 0)
    print("Результат алгоритма Прима:")
    for row in result:
        print("{0}-{1}:{2}".format(*row))


if __name__ == "__main__":
    main()
