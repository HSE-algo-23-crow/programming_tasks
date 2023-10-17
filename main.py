from typing import Any


def generate_permutations(items: frozenset[Any]) -> list[Any]:
    """Генерирует все варианты перестановок элементов указанного множества
    :param items: неизменяемое множество элементов
    :raise TypeError: если параметр items не является неизменяемым множеством
    :return: список перестановок, где каждая перестановка список элементов
    множества
    """
    validate_set_raises_ex(items)

    if len(items) == 0:
        return []

    result = []
    indexes = [0 for i in range(len(items))]
    items = list(items)
    result.append(items[:])
    i = 1
    while i < len(items):
        if indexes[i] < i:
            if i % 2 == 0:
                items[0], items[i] = items[i], items[0]
            else:
                items[indexes[i]], items[i] = items[i], items[indexes[i]]
            result.append(items[:])
            indexes[i] += 1
            i = 1
        else:
            indexes[i] = 0
            i += 1
    return result


def validate_set_raises_ex(items: frozenset[Any]):
    if type(items) != frozenset:
        raise TypeError('Параметр items не является неизменяемым множеством')


def main():
    items = frozenset([1, 2, 3])
    print(generate_permutations(items))


if __name__ == '__main__':
    main()
