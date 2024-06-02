

class Paths:
    __paths = list()
    __names = dict()

    def __init__(self):
        pass

    def add_point(self, name):
        #check for bad data
        pass

        for i in self.__names.keys():
            self.__paths[i].append([])
        self.__paths.append([[] * (len(self.__names) + 1)])
        self.__names[name] = len(self.__names) + 1

    def add_path(self, name1, name2, dist):
        #check for bad data
        pass

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
        return self.__paths[point1][point2][1] / self.__paths[point1][point2][0]

    def adjust_pheromones(self, name1, name2, adjustment):
        point1 = self.__names[name1]
        point2 = self.__names[name2]
        self.__paths[point1][point2][1] += adjustment

    def vaporize_pheromones(self, k):
        for i in self.__paths:
            for j in i:
                j[1] *= k
