from typing import Any


def generate_permutations(items: frozenset[Any]) -> list[list[Any]]:
    """Генерирует все варианты перестановок элементов указанного множества
    :param items: неизменяемое множество элементов
    :raise TypeError: если параметр items не является неизменяемым множеством
    :return: список перестановок, где каждая перестановка список элементов
    множества
    """
    if not isinstance(items, frozenset):
        raise TypeError("Параметр items не является неизменяемым множеством")

    # Рекурсивная функция для генерации перестановок
    def generate_helper(current, remaining):
        if not remaining:
            permutations.append(current[:])  # Создаем копию текущей перестановки
        else:
            for item in remaining:
                current.append(item)
                new_remaining = list(remaining)
                new_remaining.remove(item)
                generate_helper(current, new_remaining)
                current.pop()  # Удаляем последний элемент для возврата к предыдущему состоянию

    permutations = []

    # Проверка на пустое множество
    if not items:
        return permutations

    generate_helper([], list(items))
    return permutations
def main():
    items = frozenset([1, 2, 3])
    print(generate_permutations(items))

if __name__ == '__main__':
    main()
