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
    return generate_premutations_rec(set([item for item in items]))

def generate_premutations_rec(items):
    if len(items) == 1:
        return [[items.pop()]]

    current_elem = items.pop()
    premutations = generate_premutations_rec(items)
    output = []

    for premutation in premutations:
        for i in range(len(premutation) + 1):
            new_premutation = premutation[:i] + [current_elem] + premutation[i:]
            output.append(new_premutation)

    return output


def main():
    items = frozenset([1, 2, 3])
    print(generate_permutations(items))


if __name__ == "__main__":
    main()
