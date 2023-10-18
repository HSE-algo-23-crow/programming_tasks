# Выполнение функции рекурсивно
def generate_permutations(elements):
    if len(elements) <= 1:
        return [elements]

    all_permutations = []

    for element in elements:
        remaining_elements = elements - {element}
        permutations_of_remaining = generate_permutations(remaining_elements)

        for perm in permutations_of_remaining:
            all_permutations.append([element] + perm)

    return all_permutations


# Выполнение функции итеративно
from itertools import permutations

def generate_permutations(elements):
    # Преобразуем множество элементов в список (если оно не является списком)
    elements = list(elements)

    # Используем itertools.permutations для генерации перестановок
    all_permutations = list(permutations(elements))

    # Преобразуем кортежи перестановок в списки
    all_permutations = [list(perm) for perm in all_permutations]

    return all_permutations