from typing import Any


def generate_permutations(items: frozenset[Any]) -> list[Any]:
    """Генерирует все варианты перестановок элементов указанного множества
    :param items: неизменяемое множество элементов
    :raise TypeError: если параметр items не является неизменяемым множеством
    :return: список перестановок, где каждая перестановка список элементов
    множества
    """
    if not isinstance(items, frozenset):
        raise TypeError("Параметр items не является неизменяемым множеством")
    if len(items) == 0:
        return []
    if len(items) == 1:
        return [list(items)]

    result = []
    for item in items:
        remainder = items - frozenset([item])
        permutations = generate_permutations(remainder)
        for permutation in permutations:
            result.append([item] + permutation)
    return result


def main():
    items = frozenset([1, 2, 3])
    print(generate_permutations(items))


if __name__ == '__main__':
    main()
