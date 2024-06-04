from final_task.yes.Structure.paths import Paths
from final_task.yes.Structure.ant import Ant

# Здесь будет исходный код разработанного алгоритма

def main():
    paths = Paths(1.0, 1.0)
    N = int(input("Введите количество городов: "))
    for i in range(N):
        paths.add_point(input("Введите имя города #"+str(i+1)+": "))
    for i in paths.names:
        for j in paths.names:
            if i != j:
                paths.add_path(i,j, float(input("Введите расстояние между "+i+" и "+j+": ")))
    ants = [Ant(paths) for i in range(N)]
    best_path = [[], float("inf")]
    for II in range(10):
        ant_paths = [None] * N
        for i in range(N):
            ants[i].set_position(paths.names[i])
            ant_paths[i] = [ants[i].get_path(),0]
            ant_paths[i][1] = paths.get_length(ant_paths[i][0])
        for i in ant_paths:
            if (best_path[1] > i[1]):
                best_path = i
        paths.vaporize_pheromones(0.9)
        for i in ant_paths:
            k = 10.0/i[1]
            for j in range(len(i[0])-1):
                paths.adjust_pheromones(i[0][j], i[0][j+1], k)
            paths.adjust_pheromones(i[0][-1], i[0][0], k)
        print(best_path)


if __name__ == '__main__':
    main()
