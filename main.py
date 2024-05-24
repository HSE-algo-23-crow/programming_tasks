COST = 'cost'
ITEMS = 'items'
WEIGHTS = 'Веса'
COSTS = 'Стоимости'
ERR_LENGTHS_NOT_EQUAL = 'Списки весов и стоимости разной длины'
ERR_TOO_MANY_ITEMS = 'Слишком большое количество предметов'
ERR_NOT_INT_WEIGHT_LIMIT = ('Ограничение вместимости рюкзака не является целым '
                            'числом')
ERR_NOT_POS_WEIGHT_LIMIT = 'Ограничение вместимости рюкзака меньше единицы'
ERR_LESS_WEIGHT_LIMIT = ('Ограничение вместимости рюкзака меньше чем '
                         'минимальный вес предмета')
ERR_NOT_LIST_TEMPL = '{0} не являются списком'
ERR_EMPTY_LIST_TEMPL = '{0} являются пустым списком'
ERR_NOT_INT_TEMPL = '{0} содержат не числовое значение'
ERR_NOT_POS_TEMPL = '{0} содержат нулевое или отрицательное значение'


def get_knapsack(weights: list[int], costs: list[int], weight_limit: int) -> \
        dict[str, int | list[int]]:
    """Решает задачу о рюкзаке с использованием полного перебора.

    :param weights: Список весов предметов для рюкзака.
    :param costs: Список стоимостей предметов для рюкзака.
    :param weight_limit: Ограничение вместимости рюкзака.
    :raise TypeError: Если веса или стоимости не являются списком с числовыми
    значениями, если ограничение вместимости не является целым числом.
    :raise ValueError: Если в списках присутствует нулевое или отрицательное
    значение.
    :return: Словарь с ключами: cost - максимальная стоимость предметов в
    рюкзаке, items - список с индексами предметов, обеспечивающих максимальную
    стоимость.
    """
    validate_knapsack_data(weights, costs, weight_limit)
    n = len(weights)

    max_mask = ''
    max_cost = 0

    for i in range(0, 2 ** n):
        mask = bin(i)[2:]
        mask = '0' * (n - len(mask)) + mask
        if sum(weights[i] if value == '1' else 0 for i, value in enumerate(mask)) > weight_limit:
            continue

        cost = get_knapsack_cost(mask, weights, costs)
        if cost > max_cost:
            max_cost = cost
            max_mask = mask

    result = []
    for i, value in enumerate(max_mask):
        if value != '0':
            result.append(i)

    return {
        COST: max_cost,
        ITEMS: result
    }


def get_knapsack_cost(mask: str, weights: list[int], costs: list[int]):
    weight = 0
    cost = 0
    for i, value in enumerate(mask):
        if value == '0':
            continue
        cost += costs[i]
        weight += weights[i]
    return cost

def validate_knapsack_data(weights: list[int], costs: list[int], weight_limit: int):
    validate_knapsack_list(weights, WEIGHTS)
    validate_knapsack_list(costs, COSTS)
    validate_weight_limit(weights, weight_limit)

    if len(weights) != len(costs):
        raise ValueError(ERR_LENGTHS_NOT_EQUAL)

    if len(weights) > 16:
        # Добавлено именно такое ограничение, поскольку при n > 16, количество операций будет больше ста тысяч
        # и время выполнения алгоритма серьезно ухудшается и он выполняется достаточно долго
        raise ValueError(ERR_TOO_MANY_ITEMS)

def validate_weight_limit(weights: list[int], weight_limit: int):
    if type(weight_limit) is not int:
        raise TypeError(ERR_NOT_INT_WEIGHT_LIMIT)
    if weight_limit < 1:
        raise ValueError(ERR_NOT_POS_WEIGHT_LIMIT)
    if weight_limit < min(weights):
        raise ValueError(ERR_LESS_WEIGHT_LIMIT)


def validate_knapsack_list(data: list[int], name: str):
    if not isinstance(data, list):
        raise TypeError(ERR_NOT_LIST_TEMPL.format(name))
    if len(data) == 0:
        raise ValueError(ERR_EMPTY_LIST_TEMPL.format(name))
    if any(not isinstance(elem, int) for elem in data):
        raise TypeError(ERR_NOT_INT_TEMPL.format(name))
    if any(elem <= 0 for elem in data):
        raise ValueError(ERR_NOT_POS_TEMPL.format(name))








if __name__ == '__main__':
    weights = [11, 4, 8, 6, 3, 5, 5]
    costs = [17, 6, 11, 10, 5, 8, 6]
    weight_limit = 30
    print('Пример решения задачи о рюкзаке\n')
    print(f'Веса предметов для комплектования рюкзака: {weights}')
    print(f'Стоимости предметов для комплектования рюкзака: {costs}')
    print(f'Ограничение вместимости рюкзака: {weight_limit}')
    result = get_knapsack(weights, costs, weight_limit)
    print(f'Максимальная стоимость: {result[COST]}, '
          f'индексы предметов: {result[ITEMS]}')
