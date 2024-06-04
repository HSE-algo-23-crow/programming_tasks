from final_task.yes.Structure.paths import Paths
from final_task.yes.Structure.ant import Ant
from final_task.yes.errors.ers import (ALPHA_VALUE_ERROR, BETA_VALUE_ERROR,
                                       CITIES_NUMBER_ERROR, Q_VALUE_ERROR,
                                       ITERATIONS_NUMBER_ERROR, DISTANCE_NEGATIVE_ERROR,
                                       PATH_NOT_FOUND_ERROR)


def check_params(a: float, b: float, q: float, N: int, it: int):
    if a < 0: raise ValueError(ALPHA_VALUE_ERROR.format(a))
    if b < 0: raise ValueError(BETA_VALUE_ERROR.format(b))
    if q < 0: raise ValueError(Q_VALUE_ERROR.format(q))
    if N < 2: raise ValueError(CITIES_NUMBER_ERROR.format(N))
    if it < 1 or it > 10000: raise ValueError(ITERATIONS_NUMBER_ERROR.format(it))


def check_distance(d: float):
    if d < 0: raise ValueError(DISTANCE_NEGATIVE_ERROR.format(d))


def check_path(p: Paths):
    try:
        N = len(p.get_paths())
        ants = [Ant(p) for i in range(N)]
        ant_paths = [None] * N
        for i in range(N):
            ants[i].set_position(p.names[i])
            ant_paths[i] = [ants[i].get_path(), 0]
            ant_paths[i][1] = p.get_length(ant_paths[i][0])
    except KeyError:
        raise UserWarning(PATH_NOT_FOUND_ERROR)



def set_params():
    a = float(input("Введите параметр альфа алгоритма: "))
    b = float(input("Введите параметр бета алгоритма: "))
    print()
    q = float(input("Какое количество феромона выдать муравью: "))
    it = int(input("Введите количество итераций алгоритма: "))
    print()
    N = int(input("Введите количество городов: "))

    check_params(a, b, q, N, it)

    return a, b, q, N, it


def main():
    a, b, q, N, iterations = set_params()

    paths = Paths(a, b)
    for i in range(N):
        paths.add_point(input("Введите имя города #" + str(i + 1) + ": "))

    for i in paths.names:
        for j in paths.names:
            if i != j:
                distance = float(input("Введите расстояние между " + i + " и " + j + ": "))
                check_distance(distance)
                paths.add_path(i, j, distance)

    check_path(paths)

    ants = [Ant(paths) for i in range(N)]
    best_path = [[], float("inf")]
    for _ in range(iterations):

        ant_paths = [None] * N
        for i in range(N):
            ants[i].set_position(paths.names[i])
            ant_paths[i] = [ants[i].get_path(), 0]
            ant_paths[i][1] = paths.get_length(ant_paths[i][0])

        for i in ant_paths:
            if best_path[1] > i[1]:
                best_path = i

        paths.vaporize_pheromones(0.9)
        for i in ant_paths:
            k = q / i[1]
            for j in range(len(i[0]) - 1):
                paths.adjust_pheromones(i[0][j], i[0][j + 1], k)
            paths.adjust_pheromones(i[0][-1], i[0][0], k)
        print(best_path)


if __name__ == '__main__':
    main()
