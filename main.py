from typing import Any


def generate_permutations(items: frozenset[Any]) -> list[Any]:
    """Генерирует все варианты перестановок элементов указанного множества
    :param items: неизменяемое множество элементов
    :raise TypeError: если параметр items не является неизменяемым множеством
    :return: список перестановок, где каждая перестановка список элементов
    множества
    """

    if type(items) != frozenset:
        raise TypeError("Параметр items не является неизменяемым множеством")

    if len(items) == 0:
        return []

    if len(items) == 1:
        return [list(items)]

    permutations = []
    for element in items:
        remaining_elements = items - frozenset([element])
        sub_permutations = generate_permutations(remaining_elements)
        for sub_permutation in sub_permutations:
            permutations.append([element] + list(sub_permutation))

    return permutations


def main():
    items = frozenset([])
    print(generate_permutations(items))


if __name__ == '__main__':
    main()
