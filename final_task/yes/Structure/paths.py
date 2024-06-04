import random

class Paths:
    length = 0
    names = []

    __paths = list()
    __names = dict()

    __a = 1.0
    __b = 1.0

    def __init__(self, a, b):
        self.__a = a
        self.__b = b
        pass

    def get_paths(self) -> list:
        return self.__paths

    def set_paths(self, value):
        self.__paths = value

    def add_point(self, name):
        self.length += 1
        for i in self.__names.values():
            self.__paths[i].append([None, 1])

        self.__paths.append([[None, 1] for k in range(self.length)])
        self.__names[name] = self.length-1
        self.names.append(name)

    def add_path(self, name1, name2, dist):
        point1 = self.__names[name1]
        point2 = self.__names[name2]
        self.__paths[point1][point2][0] = dist

    def get_path(self, name1, name2):
        point1 = self.__names[name1]
        point2 = self.__names[name2]
        return self.__paths[point1][point2][0]

    def get_probability(self, name1, name2):
        point1 = self.__names[name1]
        point2 = self.__names[name2]
        return self.__paths[point1][point2][1]**self.__a / self.__paths[point1][point2][0]**self.__b

    def get_next_point(self, name1, visited):
        points = list(set(self.__names.keys()).difference(set(visited)))

        probabilities = [self.get_probability(name1, i) for i in points]
        sm = sum(probabilities)
        choice = random.random()*sm

        stack = 0
        for i in range(len(points)):
            stack += probabilities[i]
            if stack > choice:
                return points[i]

    def adjust_pheromones(self, name1, name2, adjustment):
        point1 = self.__names[name1]
        point2 = self.__names[name2]
        self.__paths[point1][point2][1] += adjustment

    def vaporize_pheromones(self, k):
        for i in self.__paths:
            for j in i:
                j[1] *= k

    def get_length(self, path):
        length = 0
        for i in range(len(path)-1):
            length += self.get_path(path[i], path[i+1])
        length += self.get_path(path[-1], path[0])

        return length
