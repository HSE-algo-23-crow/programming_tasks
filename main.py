COST = 'cost'
ITEMS = 'items'
WEIGHTS = 'Веса'
COSTS = 'Стоимости'
ERR_LENGTHS_NOT_EQUAL = 'Списки весов и стоимости разной длины'
ERR_NOT_INT_WEIGHT_LIMIT = ('Ограничение вместимости рюкзака не является целым числом')
ERR_NOT_POS_WEIGHT_LIMIT = 'Ограничение вместимости рюкзака меньше единицы'
ERR_LESS_WEIGHT_LIMIT = ('Ограничение вместимости рюкзака меньше чем минимальный вес предмета')
ERR_NOT_LIST_TEMPL = '{0} не являются списком'
ERR_EMPTY_LIST_TEMPL = '{0} являются пустым списком'
ERR_NOT_INT_TEMPL = '{0} содержат не числовое значение'
ERR_NOT_POS_TEMPL = '{0} содержат нулевое или отрицательное значение'
ERR_LEN = 'Кол-во предметов превышает лимит (21)'

def get_knapsack(weights: list[int], costs: list[int], weight_limit: int) -> dict[str, int | list[int]]:
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
    validate_params(weights, costs, weight_limit)

    all_variants = 2 ** len(weights)
    max_cost = 0
    best_variant = ''

    for i in range(1, all_variants):
        variant = bin(i)[2:].zfill(len(weights))
        cur_weight, cur_cost = 0, 0

        for j in range(len(variant)):
            if variant[j] == '1':
                cur_weight += weights[j]
                if cur_weight > weight_limit:
                    cur_cost = 0
                    break
                cur_cost += costs[j]

        if max_cost < cur_cost:
            best_variant = variant
            max_cost = cur_cost

    items = [i for i in range(len(best_variant)) if best_variant[i] == '1']
    return {'cost': max_cost, 'items': items}

def validate_params(weights: list[int], costs: list[int], weight_limit: int):
    validate_lists(weights, WEIGHTS)
    validate_lists(costs, COSTS)
    if len(weights) != len(costs):
        raise ValueError(ERR_LENGTHS_NOT_EQUAL)
    if not isinstance(weight_limit, int):
        raise TypeError(ERR_NOT_INT_WEIGHT_LIMIT)
    if weight_limit < 1:
        raise ValueError(ERR_NOT_POS_WEIGHT_LIMIT)
    if weight_limit < min(weights):
        raise ValueError(ERR_LESS_WEIGHT_LIMIT)
    if len(weights) > 21:
        raise ValueError(ERR_LEN)

def validate_lists(this_list, name):
    if not isinstance(this_list, list):
        raise TypeError(ERR_NOT_LIST_TEMPL.format(name))
    if not all(isinstance(item, int) for item in this_list):
        raise TypeError(ERR_NOT_INT_TEMPL.format(name))
    if len(this_list) == 0:
        raise ValueError(ERR_EMPTY_LIST_TEMPL.format(name))
    if any(item <= 0 for item in this_list):
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
    print(f'Максимальная стоимость: {result[COST]}, индексы предметов: {result[ITEMS]}')