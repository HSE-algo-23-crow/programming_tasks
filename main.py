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
ERR_ENORMOUS_SIZE = 'Слишком большой размер списка ({0})'


def limit_verify(weight_limit: int) -> None:
    if not isinstance(weight_limit, int): raise TypeError(ERR_NOT_INT_WEIGHT_LIMIT)
    if weight_limit <= 0: raise ValueError(ERR_NOT_POS_WEIGHT_LIMIT)


def costs_verify(cs: list[int]) -> None:
    if not isinstance(cs, list): raise TypeError(ERR_NOT_LIST_TEMPL.format(COSTS))
    if not cs: raise ValueError(ERR_EMPTY_LIST_TEMPL.format(COSTS))
    if len(cs) > 50: raise ValueError(ERR_ENORMOUS_SIZE.format(len(cs)))
    for c in cs:
        if not isinstance(c, int): raise TypeError(ERR_NOT_INT_TEMPL.format(COSTS))
        if c <= 0: raise ValueError(ERR_NOT_POS_TEMPL.format(COSTS))


def weights_verify(ws: list[int]) -> None:
    if not isinstance(ws, list): raise TypeError(ERR_NOT_LIST_TEMPL.format(WEIGHTS))
    if not ws: raise ValueError(ERR_EMPTY_LIST_TEMPL.format(WEIGHTS))
    if len(ws) > 50: raise ValueError(ERR_ENORMOUS_SIZE.format(len(ws)))
    for w in ws:
        if not isinstance(w, int): raise TypeError(ERR_NOT_INT_TEMPL.format(WEIGHTS))
        if w <= 0: raise ValueError(ERR_NOT_POS_TEMPL.format(WEIGHTS))


def combined_verify(ws: list[int], cs: list[int], wl: int) -> None:
    if len(ws) != len(cs): raise ValueError(ERR_LENGTHS_NOT_EQUAL)
    if min(ws) > wl: raise ValueError(ERR_LESS_WEIGHT_LIMIT)


def params_verify(ws: list[int], cs: list[int], wl: int) -> None:
    limit_verify(wl)
    costs_verify(cs)
    weights_verify(ws)
    combined_verify(ws, cs, wl)


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

    params_verify(weights, costs, weight_limit)

    result_cost = 0
    result_items = []
    for number_of_items_in_combination in range(len(costs)):
        for combination in itertools.combinations(range(len(costs)), number_of_items_in_combination+1):

            current_cost = 0
            current_weight = 0

            for index in combination:
                current_cost += costs[index]
                current_weight += weights[index]

            if current_cost > result_cost and current_weight <= weight_limit:
                result_cost, result_items = current_cost, list(combination)

    return {COST: result_cost, ITEMS: result_items}


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
