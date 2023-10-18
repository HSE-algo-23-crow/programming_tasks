from typing import Any


def generate_permutations(items: frozenset[Any]) -> list[Any]:
    #Проверка типа
    if not isinstance(items, frozenset):
        raise TypeError('Параметр items не является неизменяемым множеством')

    #Копируем набор элементов
    temp_items = set(items)

    #Проверка пустого множества
    if (len(temp_items)) == 0:
        return []

    output = [[temp_items.pop(), ], ]
    #Перебор всех элементов
    for iteration in range(len(temp_items)):
        temp_list = []
        item = temp_items.pop()
        #Перебор имеющихся вариантов
        for element_number in range(len(output)):
            #Перебор индексов для вставки
            for item_index in range(len(output[0])+1):
                temp = list(output[element_number])
                temp.insert(item_index, item)
                temp_list.append(temp)
        output = temp_list
    return output


def main():
    items = frozenset([1, 2, 3])
    print(generate_permutations(items))


if __name__ == '__main__':
    main()
