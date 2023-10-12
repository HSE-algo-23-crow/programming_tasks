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
        return [[x for x in items]]
    return generate_premutations_rec(items)

def generate_premutations_rec(items):
    if len(items) <= 1:
        return [items]

    result = []
    elems = list(items)
    for i in range(len(elems)):
        remaining_elements = elems[:i] + elems[i + 1 :]
        permutations = generate_premutations_rec(frozenset(remaining_elements))

        for permutation in permutations:
            result.append([elems[i]] + list(permutation))

    return result

def main():
    items = frozenset([1, 2, 3])
    print(generate_permutations(items))


if __name__ == "__main__":
    main()
