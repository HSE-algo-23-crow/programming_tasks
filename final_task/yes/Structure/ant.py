from final_task.yes.Structure.paths import Paths

class Ant:

    __paths = None
    __position = None
    __visited = []

    def __init__(self, paths : Paths):
        self.__paths = paths
        self.__visited = []

    def set_position(self, position):
        self.__position = position
        self.__visited.append(position)

    def __step(self):
        next_point = self.__paths.get_next_point(self.__position, self.__visited)
        self.__position = next_point
        self.__visited.append(self.__position)

    def get_path(self):
        while len(self.__visited) < self.__paths.length:
            self.__step()

        path = self.__visited
        self.__visited = []
        self.__position = None

        return path
