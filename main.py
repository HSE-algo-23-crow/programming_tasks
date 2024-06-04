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


def get_list_full_validation(obj_list, obj_name):

    # not list check
    if not(isinstance(obj_list, list)):
        raise TypeError(ERR_NOT_LIST_TEMPL.format(obj_name))

    # not empty list check
    if len(obj_list) == 0:
        raise ValueError(ERR_EMPTY_LIST_TEMPL.format(obj_name))

    # only positive ints in list check
    for item in obj_list:
        if not(isinstance(item, int)):
            raise TypeError(ERR_NOT_INT_TEMPL.format(obj_name))
        elif item <= 0:
            raise ValueError(ERR_NOT_POS_TEMPL.format(obj_name))


def get_validate_params(wghts, csts, wght_lmt):

    get_list_full_validation(wghts, WEIGHTS)
    get_list_full_validation(csts, COSTS)

    if len(wghts) != len(csts):
        raise ValueError(ERR_LENGTHS_NOT_EQUAL)

    if not(isinstance(wght_lmt, int)):
        raise TypeError(ERR_NOT_INT_WEIGHT_LIMIT)

    if wght_lmt <= 0:
        raise ValueError(ERR_NOT_POS_WEIGHT_LIMIT)

    if wght_lmt < min(wghts):
        raise ValueError(ERR_LESS_WEIGHT_LIMIT)


def generate_cases(items_count):
    cases = []

    for number in range(1, 2 ** items_count):
        defective_case = bin(number)[2:]
        case = "0" * (items_count - len(defective_case)) + defective_case
        cases.append(case)

    return cases


def get_weight_and_cost_for_case(cur_case, weights_list, costs_list):
    case_weight = 0
    case_cost = 0

    for i in range(len(cur_case)):
        if cur_case[i] == "1":
            case_weight += weights_list[i]
            case_cost += costs_list[i]

    return case_weight, case_cost


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

    get_validate_params(weights, costs, weight_limit)

    max_cost = 0
    max_case = None
    cases = generate_cases(len(weights))

    for case in cases:
        case_weight, case_cost = get_weight_and_cost_for_case(case, weights, costs)
        if case_weight <= weight_limit:
            if case_cost > max_cost:
                max_cost = case_cost
                max_case = case

    max_case_items = []
    for i in range(len(max_case)):
        if max_case[i] == "1":
            max_case_items.append(i)

    return {COST: max_cost, ITEMS: max_case_items}


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
