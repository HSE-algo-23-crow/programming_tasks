from typing import Any


def generate_permutations(items: frozenset[Any]) -> list[Any]:
    """Функция-обертка проверяет пар. items на принадлежность типу frozenset, а также возвращает пустое множество, если
    в items нет элементов для генерации перестановок

    :param items: неизменяемое множество элементов
    :raise TypeError: если параметр items не является неизменяемым множеством
    :return: список перестановок, где каждая перестановка список элементов (через рекурсивную функцию)
    множества
    """

    if type(items) != frozenset:
        raise TypeError("Параметр items не является неизменяемым множеством")

    if len(items) == 0:
        return []

    return get_permutations_recursive(set([item for item in items]))


def get_permutations_recursive(items):
    """Рекурсивная функция для генерации всех перестановок из элементов items типа frozenset

    :param items: неизменяемое множество элементов
    :return: список перестановок, где каждая перестановка список элементов
    """

    if len(items) == 1:
        return [[items.pop()]]

    current_elem = items.pop()
    permutations = get_permutations_recursive(items)
    output = []

    for permute in permutations:
        for i in range(len(permute) + 1):
            new_permutation = permute[:i] + [current_elem] + permute[i:]
            output.append(new_permutation)

    return output


def main():
    items = frozenset([1, 2, 3])
    print(generate_permutations(items))


if __name__ == '__main__':
    main()
