import random as rnd

from knapsack_problem.constants import COST, ITEMS, POPULATION_LIMIT, EPOCH_CNT, \
    BRUTE_FORCE_BOUND
from knapsack_problem.brute_force import brute_force
from knapsack_problem.validate import validate_params
import itertools
from random import choice, randint


class GeneticSolver:
    """Класс для решения задачи о рюкзаке с использованием генетического
    алгоритма. Для входных данных небольшого размера используется полный
    перебор.

    Экземпляр класса хранит состояние популяции, метод поиска решения может
    быть запущен многократно для одного экземпляра.

    """

    def __init__(self, weights: list[int], costs: list[int], weight_limit: int):
        """Создает объект класса для решения задачи о рюкзаке.

        :param weights: Список весов предметов для рюкзака.
        :param costs: Список стоимостей предметов для рюкзака.
        :param weight_limit: Ограничение вместимости рюкзака.
        :raise TypeError: Если веса или стоимости не являются списком с числовыми
        значениями, если ограничение вместимости не является целым числом.
        :raise ValueError: Если в списках присутствует нулевое или отрицательное
        значение.
        """
        validate_params(weights, costs, weight_limit)
        self.__item_cnt = len(weights)
        self.__mask = '{0:0' + str(len(weights)) + 'b}'
        self.__weights = weights
        self.__costs = costs
        self.__weight_limit = weight_limit
        self.__population_cnt = min(2 ** self.__item_cnt / 2, POPULATION_LIMIT)
        self.__population = self.__generate_population(self.__population_cnt)

    @staticmethod
    def __generate_combination(self, combination_length: int) -> str:
        res = ''
        for i in range(combination_length):
            res += choice(['0', '1'])
        return res

    def __comb_weight(self, c: str) -> int:
        weight = 0
        for i in range(len(c)):
            if c[i] == '1': weight += self.__weights[i]

        return weight

    def __comb_fitness(self, c: str) -> int:
        fitness = 0
        for i in range(len(c)):
            if c[i] == '1': fitness += self.__costs[i]

        return fitness

    def __generate_population(self, population_cnt: int) -> list[tuple[str, int]]:
        result = []
        while len(result) != self.__population_cnt:
            comb = self.__generate_combination(self, self.__item_cnt)
            comb_weight = self.__comb_weight(comb)
            if comb_weight <= self.__weight_limit:
                result.append((comb, self.__comb_fitness(comb)))

        return result

    def __roulette(self, common_len: int) -> int:
        ch = randint(0, common_len)

        i = 0
        while True:
            if ch - self.__population[i][1] > 0:
                ch -= self.__population[i][1]
                i += 1
            else:
                break

        return i

    def __get_crossing(self) -> list[int]:
        result = []

        cl = 0
        for i in self.__population:
            cl += i[1]

        while len(result) != self.__population_cnt // 4:
            new = self.__roulette(cl)
            if not (new in result):
                result.append(new)

        return result

    def __mutation(self, c: str):
        while self.__comb_weight(c) > self.__weight_limit:
            ones_indices = [i for i, char in enumerate(c) if char == '1']
            random_index = choice(ones_indices)

            c = list(c)
            c[random_index] = '0'
            c = ''.join(c)

        return c

    def __cross_two(self, u1: tuple[str, int], u2: tuple[str, int]):
        barrier = randint(1, len(u1[0])-1)

        new_unit1 = u1[0][:barrier]+u2[0][barrier:]
        new_unit2 = u2[0][:barrier]+u1[0][barrier:]

        if self.__comb_weight(new_unit1) <= self.__weight_limit:
            self.__population.append((new_unit1, self.__comb_fitness(new_unit1)))
        else:
            new_unit1 = self.__mutation(new_unit1)
            self.__population.append((new_unit1, self.__comb_fitness(new_unit1)))

        if self.__comb_weight(new_unit2) <= self.__weight_limit:
            self.__population.append((new_unit2, self.__comb_fitness(new_unit2)))
        else:
            new_unit2 = self.__mutation(new_unit2)
            self.__population.append((new_unit2, self.__comb_fitness(new_unit2)))

    def __cross_population(self, crs: list[int]):
        while len(crs) != 0:
            unit1 = self.__population[crs.pop(0)]
            unit2 = self.__population[crs.pop(0)]

            self.__cross_two(unit1, unit2)

    def __cut_population(self):
        self.__population = self.__population[:int(self.__population_cnt)]

    def get_knapsack(self, epoch_cnt=EPOCH_CNT) -> dict[str, int | list[int]]:
        """Запускает генетический алгоритм для решения задачи о рюкзаке.
        Алгоритм выполняется заданное количество поколений.

        :return: Словарь с ключами: cost - максимальная стоимость предметов в
        рюкзаке, items - список с индексами предметов, обеспечивающих максимальную
        стоимость.
        """
        for _ in range(epoch_cnt):
            self.__population = sorted(self.__population, key=lambda x: -x[1])
            crossing = self.__get_crossing()
            self.__cross_population(crossing)
            self.__population = sorted(self.__population, key=lambda x: -x[1])
            self.__cut_population()

        return {COST: self.__population[0][1], ITEMS: list(i for i, v in enumerate(list(map(int, self.__population[0][0]))) if v)}

    @property
    def population(self) -> list[tuple[str, int]]:
        """Возвращает список особей текущей популяции. Для каждой особи
        возвращается строка из 0 и 1, а также значение финтес-функции.
        """
        return self.__population


if __name__ == '__main__':
    weights = [67, 30, 8, 50, 94, 24, 3, 78]
    costs = [77, 13, 38, 86, 92, 33, 46, 9]
    weight_limit = 50
    gk = GeneticSolver(weights, costs, weight_limit)
    print(gk.get_knapsack())
