from schedule_pack import Schedule, Task


"""Для решения задачи составления оптимального расписания с использованием 
Ленточной стратегии подготовлен python-пакет schedule_pack.

В пакете представлены следующие классы
    - Task: Представляет задачу для составления расписания. Используется в
    качестве входных данных для класса Schedule.
    - Schedule: Представляет оптимальное расписание для списка задач и 
    количества исполнителей. Для каждого исполнителя расписание представлено
    набором экземпляров класса ScheduleItem.
    - ScheduleItem: Представляет собой элемент расписания, включает в себя
    задачу, выполняющуюся в течение некоторого времени, с указанием моментов
    начала и окончания ее выполнения.

!!! Для выполнения задания необходимо реализовать два приватных метода 
класса Schedule, расположенного в файле schedule_pack/schedule.py:
    - __calculate_duration(self) -> float: Вычисляет и возвращает минимальную
    продолжительность расписания.
    - __fill_schedule_for_each_executor(self) -> None: Процедура составляет
    расписание из элементов ScheduleItem для каждого исполнителя, на основе
    исходного списка задач и общей продолжительности расписания.
Указанные методы используются при инициализации объекта класса Schedule 
в методе __init__.

Проверить реализацию класса Schedule можно запустив набор авто-тестов 
в файле schedule_pack/tests/test_schedule.py.

Запустить тесты для проверки всего пакета schedule_pack можно с помощью 
файла test_runner.py.

"""


def main():
    print('Пример использования класса Schedule')

    # Инициализируем входные данные для составления расписания
    tasks = [Task('a', 3), Task('b', 4), Task('c', 6), Task('d', 7),
             Task('e', 7), Task('f', 9), Task('g', 10), Task('h', 12),
             Task('i', 17)]

    # Инициализируем экземпляр класса Schedule
    # при этом будет рассчитано расписание для каждого исполнителя
    schedule = Schedule(tasks, 5)
    task_a = Task('a', 3)
    task_b = Task('b', 4)
    task_c = Task('c', 6)
    task_d = Task('d', 7)
    task_e = Task('e', 7)
    task_f = Task('f', 9)
    task_g = Task('g', 10)
    task_h = Task('h', 12)
    task_i = Task('i', 17)
    tasks = [task_a, task_b, task_c, task_d, task_e, task_f, task_g,
             task_h, task_i]
    schedule = Schedule(tasks, 5)

    # Выведем в консоль полученное расписание
    print(schedule)
    for i in range(schedule.executor_count):
        print(f'\nРасписание для исполнителя # {i + 1}:')
        for schedule_item in schedule.get_schedule_for_executor(i):
            print(schedule_item)


if __name__ == '__main__':
    main()
