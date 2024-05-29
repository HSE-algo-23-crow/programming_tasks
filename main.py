import itertools

COST = 'cost'
ITEMS = 'items'
WEIGHTS = 'Веса'
COSTS = 'Стоимости'
ERR_LENGTHS_NOT_EQUAL = 'Списки весов и стоимости разной длины'
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
    if not isinstance(weights, list):
        raise TypeError(ERR_NOT_LIST_TEMPL.format(WEIGHTS))
    if not isinstance(costs, list):
        raise TypeError(ERR_NOT_LIST_TEMPL.format(COSTS))
    if not isinstance(weight_limit, int):
        raise TypeError(ERR_NOT_INT_WEIGHT_LIMIT)
    if weight_limit < 1:
        raise ValueError(ERR_NOT_POS_WEIGHT_LIMIT)
    if not weights:
        raise ValueError(ERR_EMPTY_LIST_TEMPL.format(WEIGHTS))
    if not costs:
        raise ValueError(ERR_EMPTY_LIST_TEMPL.format(COSTS))
    if len(weights) != len(costs):
        raise ValueError(ERR_LENGTHS_NOT_EQUAL)
    if any(not isinstance(w, int) for w in weights):
        raise TypeError(ERR_NOT_INT_TEMPL.format(WEIGHTS))
    if any(not isinstance(c, int) for c in costs):
        raise TypeError(ERR_NOT_INT_TEMPL.format(COSTS))
    if any(w <= 0 for w in weights):
        raise ValueError(ERR_NOT_POS_TEMPL.format(WEIGHTS))
    if any(c <= 0 for c in costs):
        raise ValueError(ERR_NOT_POS_TEMPL.format(COSTS))
    if weight_limit < min(weights):
        raise ValueError(ERR_LESS_WEIGHT_LIMIT)

    n = len(weights)
    best_cost = 0
    best_items = []

    for r in range(1, n + 1):
        for subset in itertools.combinations(range(n), r):
            subset_weight = sum(weights[i] for i in subset)
            subset_cost = sum(costs[i] for i in subset)
            if subset_weight <= weight_limit and subset_cost > best_cost:
                best_cost = subset_cost
                best_items = list(subset)

    return {COST: best_cost, ITEMS: best_items}



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
