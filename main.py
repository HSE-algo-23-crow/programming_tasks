def get_win_sequence(input_string: str) -> str:
    """Вычисляет минимальную лексикографическую подпоследовательность строки,
    получаемую из исходной строки путем отбрасывания некоторого числа символов
    с начала.

    :param input_string: Параметры текстом. В первой строке целое число, длина
    исходной строки, во второй строке последовательность из заглавных латинских
    букв длинной не менее, заданной первым параметром.
    :return: Строку, представляющую минимальную лексикографическую
    подпоследовательность исходной строки.
    """
    line = list(input_string.split("\n"))
    n = int(line[0])
    string = line[1][:n]
    min_letter = min(string)
    sequences = []
    for i in range(len(string)):
        if string[i] == min_letter:
            sequences.append(string[i:])
    return min(sequences)
def get_water_volume(input_string: str) -> int:
    """Вычисляет объем воды (количество блоков), который остается после дождя
    на острове.

    :param input_string: Параметры текстом. В первой строке целое число,
    количество столбцов, представляющих ландшафт острова, во второй строке
    список целых чисел, высоты столбцов.
    :return: Целое число, представляющее объем воды (в блоках), который
    останется после дождя.
    """
    input_string = list(input_string.split("\n"))
    n = int(input_string[0])
    heights = list(map(int, str(input_string[1]).split()))
    left_maxes = [0] * n
    right_maxes = [0] * n

    left_maxes[0] = heights[0]
    for i in range(1, n):
        left_maxes[i] = max(left_maxes[i - 1], heights[i])  # ищем все максимумы слева и записываем в список
    right_maxes[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_maxes[i] = max(right_maxes[i + 1], heights[i])  # ищем все максимумы справа и записываем в список
    count = 0
    for i in range(n):
        count += min(left_maxes[i], right_maxes[i]) - heights[
            i]  # исчитаем блоки с водой, берем мин высоту правого и левого максимума для данной вершины и вычитаем ее высоту
    return count


def main():
    print(get_water_volume('11\n2 5 2 3 6 9 3 1 3 4 6'))  # 18

    print(get_win_sequence('4\nMAMA'))  # A
    print(get_win_sequence('8\nALLOALLO'))  # ALLO
    print(get_win_sequence('21\nASZYAFAXZEWWAVQHJHBPELYZP'))  # ABCOAX


if __name__ == '__main__':
    main()
