import random
from typing import Callable, TypeVar

STAGE = 0
WIN = 1
LOOS = 2
T = TypeVar('T')


def tournament_validation(sample, function):
    if not isinstance(sample, (list, tuple)):
        raise TypeError("Sample for a tournament is not a list or a tuple")
    if len(sample) < 2:
        raise ValueError('Sample for the tournament consists of less than two objects')
    if not callable(function):
        raise TypeError('get_winner is not a function')
    winner = function(sample[0], sample[1])
    if winner not in sample:
        raise RuntimeError('get_winner function returned an invalid value')
def select_winner(sample, get_winner):
    if len(sample) == 1:
        return sample[0]
    next_round = []

    # Проводим турниры между парами объектов.
    for i in range(0, len(sample), 2):
        if i + 1 < len(sample):
            winner = get_winner(sample[i], sample[i + 1])
            if winner not in sample:
                raise RuntimeError('get_winner function returned an invalid value')
            next_round.append(winner)
        else:
            # Если объект без пары, он автоматически переходит в следующий раунд.
            next_round.append(sample[i])
    return select_winner(next_round, get_winner)

def tournament(sample: list[T] | tuple[T], get_winner: Callable[[T, T], T]):
    """Выполняет турнирный отбор из заданной выборки. Проводит серию турниров
    между парами объектов из выборки. Победители каждого турнира переходят на
    следующий этап, пока не останется один победитель.

    :param sample: Выборка для проведения турнира.
    :param get_winner: Функция для выбора победителя из двух объектов.
    :raises TypeError: Если выборка объектов не является списком или кортежем
    или функция выбора победителя имеет некорректный тип.
    :raises ValueError: Если выборка объектов пуста.
    :raises RuntimeError: Если функция get_winner возвращает некорректное
    значение.
    :return: Объект победитель турнира.
    """
    tournament_validation(sample, get_winner)
    winner = select_winner(sample, get_winner)
    return winner



if __name__ == '__main__':
    sample = [i for i in range(21)]
    random.shuffle(sample)

    print(f'Список: {sample}')
    print(f'Победитель турнира: {tournament(sample, lambda x, y: max(x, y))}')
