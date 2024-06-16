import random as rnd
from knapsack_problem.constants import COST, ITEMS, POPULATION_LIMIT, EPOCH_CNT, BRUTE_FORCE_BOUND
from knapsack_problem.brute_force import brute_force
from knapsack_problem.validate import validate_params

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

    def fitness(self, individual):
        total_weight = sum(self.__weights[i] for i in range(self.__item_cnt) if individual[i] == 1)
        total_value = sum(self.__costs[i] for i in range(self.__item_cnt) if individual[i] == 1)
        if total_weight > self.__weight_limit:
            return 0
        else:
            return total_value

    def get_two_best(self, population):
        non_zero_population = [ind for ind in population if self.fitness(ind) > 0]
        if len(non_zero_population) < 2:
            return rnd.sample(population, 2)
        weights = [self.fitness(ind) for ind in non_zero_population]
        return rnd.choices(non_zero_population, weights=weights, k=2)

    def crossover(self, parent1, parent2):
        point = rnd.randint(1, self.__item_cnt - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

    def mutation(self, individual):
        if rnd.random() < 0.1:
            point = rnd.randint(0, self.__item_cnt - 1)
            individual[point] = 1 - individual[point]
        return individual

    def genetic_algorithm(self):
        population = self.__population
        for _ in range(EPOCH_CNT):
            new_population = set()
            while len(new_population) < self.__population_cnt:
                parent1, parent2 = self.get_two_best(population)
                child1, child2 = self.crossover(parent1, parent2)
                new_population.add(tuple(self.mutation(child1)))
                if len(new_population) < self.__population_cnt:
                    new_population.add(tuple(self.mutation(child2)))
            population = [list(ind) for ind in new_population]
        return max(population, key=self.fitness)

    @property
    def population(self):
        """Возвращает список особей текущей популяции. Для каждой особи
        возвращается строка из 0 и 1, а также значение финтес-функции.
        """
        return [(self.__mask.format(int("".join(map(str, ind)), 2)), self.fitness(ind)) for ind in self.__population]

    def get_knapsack(self, epoch_cnt=EPOCH_CNT):
        """Запускает генетический алгоритм для решения задачи о рюкзаке.
        Алгоритм выполняется заданное количество поколений.
        
        :return: Словарь с ключами: cost - максимальная стоимость предметов в
        рюкзаке, items - список с индексами предметов, обеспечивающих максимальную
        стоимость.
        """
        global EPOCH_CNT
        EPOCH_CNT = epoch_cnt
        best_individual = self.genetic_algorithm()
        best_cost = self.fitness(best_individual)
        best_items = [i for i, gene in enumerate(best_individual) if gene == 1]
        return {'cost': best_cost, 'items': best_items}

if __name__ == '__main__':
    weights = [67, 30, 8, 50, 94, 24, 3, 78]
    costs = [77, 13, 38, 86, 92, 33, 46, 9]
    weight_limit = 50
    gk = GeneticSolver(weights, costs, weight_limit)
    print(gk.get_knapsack())
