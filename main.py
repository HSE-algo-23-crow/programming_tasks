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
        return list()

    def next_permutation(arr):
        n = len(arr)
        i = n - 2

        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        if i == -1:
            return None

        j = n - 1

        while arr[j] <= arr[i]:
            j -= 1

        arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1:] = arr[i + 1:][::-1]

        return arr

    elements_list = list(items)
    elements_list.sort()
    permutations = [elements_list[:]]

    next_perm = next_permutation(elements_list)
    while next_perm:
        permutations.append(next_perm.copy())
        next_perm = next_permutation(next_perm)

    return permutations


def main():
    items = frozenset([1, 2, 3])
    print(generate_permutations(items))


if __name__ == '__main__':
    main()
