import random as rnd
from knapsack_problem.constants import COST, ITEMS, POPULATION_LIMIT, EPOCH_CNT, BRUTE_FORCE_BOUND
from knapsack_problem.brute_force import brute_force
from knapsack_problem.validate import validate_params
from functools import lru_cache

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
        self.__population_cnt = min(2 ** self.__item_cnt // 2, POPULATION_LIMIT)
        self.__population = self.__generate_population(self.__population_cnt)

    def __generate_population(self, size):
        population = set()
        while len(population) < size:
            individual = tuple(rnd.randint(0, 1) for _ in range(self.__item_cnt))
            population.add(individual)
        return [list(ind) for ind in population]

    @lru_cache(None)
    def fitness(self, individual):
        total_weight = sum(w for w, i in zip(self.__weights, individual) if i)
        total_value = sum(c for c, i in zip(self.__costs, individual) if i)
        return total_value if total_weight <= self.__weight_limit else 0

    def select_parents(self, population):
        non_zero_population = [ind for ind in population if self.fitness(tuple(ind)) > 0]
        if len(non_zero_population) < self.__population_cnt:
            non_zero_population.extend(rnd.choices(population, k=self.__population_cnt - len(non_zero_population)))
        weights = [self.fitness(tuple(ind)) for ind in non_zero_population]
        parents = rnd.choices(non_zero_population, weights=weights, k=self.__population_cnt)
        return parents

    def crossover(self, parent1, parent2):
        point = rnd.randint(1, self.__item_cnt - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

    def mutation(self, individual):
        if rnd.random() < 0.1:
            point = rnd.randint(0, self.__item_cnt - 1)
            individual[point] = 1 - individual[point]
        return individual

    def genetic_algorithm(self, epoch_cnt):
        population = self.__population
        for _ in range(epoch_cnt):
            parents = self.select_parents(population)
            new_population = set()
            for i in range(0, len(parents), 2):
                parent1 = parents[i]
                parent2 = parents[i + 1] if i + 1 < len(parents) else parents[0]
                child1, child2 = self.crossover(parent1, parent2)
                new_population.add(tuple(self.mutation(child1)))
                if len(new_population) < self.__population_cnt:
                    new_population.add(tuple(self.mutation(child2)))
            population = [list(ind) for ind in new_population]
        self.__population = population
        return max(population, key=lambda ind: self.fitness(tuple(ind)))

    @property
    def population(self):
        """Возвращает список особей текущей популяции. Для каждой особи
        возвращается строка из 0 и 1, а также значение финтес-функции.
        """
        return [(self.__mask.format(int("".join(map(str, ind)), 2)), self.fitness(tuple(ind))) for ind in self.__population]

    def get_knapsack(self, epoch_cnt=EPOCH_CNT):
        """Запускает генетический алгоритм для решения задачи о рюкзаке.
        Алгоритм выполняется заданное количество поколений.

        :return: Словарь с ключами: cost - максимальная стоимость предметов в
        рюкзаке, items - список с индексами предметов, обеспечивающих максимальную
        стоимость.
        """
        best_individual = self.genetic_algorithm(epoch_cnt)
        best_cost = self.fitness(tuple(best_individual))
        best_items = [i for i, gene in enumerate(best_individual) if gene == 1]
        return {'cost': best_cost, 'items': best_items}


if __name__ == '__main__':
    weights = [67, 30, 8, 50, 94, 24, 3, 78]
    costs = [77, 13, 38, 86, 92, 33, 46, 9]
    weight_limit = 50
    gk = GeneticSolver(weights, costs, weight_limit)
    print(gk.get_knapsack())
