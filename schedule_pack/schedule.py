from schedule_pack.task import Task
from schedule_pack.schedule_item import ScheduleItem
from schedule_pack.errors import ScheduleArgumentError
from schedule_pack.constants import ERR_TASKS_NOT_LIST_MSG,\
    ERR_TASKS_EMPTY_LIST_MSG, ERR_INVALID_TASK_TEMPL, \
    ERR_EXECUTOR_NOT_INT_MSG, ERR_EXECUTOR_OUT_OF_RANGE_MSG, SCHEDULE_STR_TEMPL


class Schedule:
    """Класс представляет оптимальное расписание для списка задач и количества
    исполнителей. Для построения расписания используется Ленточная стратегия.

    Properties
    ----------
    tasks(self) -> tuple[Task]:
        Возвращает исходный список задач для составления расписания.

    task_count(self) -> int:
        Возвращает количество задач для составления расписания.

    executor_count(self) -> int:
        Возвращает количество исполнителей.

    duration(self) -> float:
        Возвращает общую продолжительность расписания.

    Methods
    -------
    get_schedule_for_executor(self, executor_idx: int) -> tuple[ScheduleRow]:
        Возвращает расписание для указанного исполнителя.
    """

    def __init__(self, tasks: list[Task], executor_count: int):
        """Конструктор для инициализации объекта расписания.

        :param tasks: Список задач для составления расписания.
        :param executor_count: Количество исполнителей.
        :raise ScheduleArgumentError: Если список задач предоставлен в
        некорректном формате или количество исполнителей не является целым
        положительным числом.
        """
        Schedule.__validate_params(tasks)

        # Сохраняем исходный список задач в приватном поле класса
        self.__tasks = tasks

        # Для каждого исполнителя создается пустая заготовка для расписания
        self.__executor_schedule: list[list[ScheduleItem]] = \
            [[] for _ in range(executor_count)]

        # Рассчитывается и сохраняется в приватном поле класса минимальная
        # продолжительность расписания
        self.__duration = self.__calculate_duration()

        # Процедура заполняет пустую заготовку расписания для каждого
        # исполнителя объектами ScheduleItem.
        self.__fill_schedule_for_each_executor()

    def __str__(self):
        return SCHEDULE_STR_TEMPL.format(self.duration, self.task_count,
                                         self.executor_count)

    @property
    def tasks(self) -> tuple[Task]:
        """Возвращает исходный список задач для составления расписания."""
        return tuple(self.__tasks)

    @property
    def task_count(self) -> int:
        """Возвращает количество задач для составления расписания."""
        return len(self.__tasks)

    @property
    def executor_count(self) -> int:
        """Возвращает количество исполнителей."""
        return len(self.__executor_schedule)

    @property
    def duration(self) -> float:
        """Возвращает общую продолжительность расписания."""
        return self.__duration

    def get_schedule_for_executor(self, executor_idx: int) -> \
            tuple[ScheduleItem]:
        """Возвращает расписание для указанного исполнителя.

        :param executor_idx: Индекс исполнителя.
        :raise ScheduleArgumentError: Если индекс исполнителя не является целым
         положительным числом или превышает количество исполнителей.
        :return: Расписание для указанного исполнителя.
        """
        self.__validate_executor_idx(executor_idx)
        return tuple(self.__executor_schedule[executor_idx])

    def __calculate_duration(self) -> float:
        """Вычисляет и возвращает минимальную продолжительность расписания"""
        # Вычисляем Tmax - максимальную продолжительность среди всех заданий
        Tmax = max(task.duration for task in self.__tasks)

        # Вычисляем сумму продолжительностей всех задач
        total_duration = sum(task.duration for task in self.__tasks)

        # Вычисляем Tavg - среднюю продолжительность задач для одного исполнителя
        Tavg = total_duration / len(self.__executor_schedule)

        # Возвращаем максимальное значение из Tmax и Tavg
        return max(Tmax, Tavg)

    def __fill_schedule_for_each_executor(self) -> None:
        schedule_duration = self.__duration
        # Очередь задач с оставшимся временем
        task_queue = [(task, task.duration) for task in self.__tasks]
        # Отслеживаем использованное время для каждого исполнителя
        executor_time_used = [0] * len(self.__executor_schedule)

        # Проходим по каждому исполнителю и пытаемся назначить задачи
        for executor_index in range(len(self.__executor_schedule)):
            while task_queue and executor_time_used[executor_index] < schedule_duration:
                task, remaining_duration = task_queue[0]  # Смотрим первую задачу в очереди

                # Вычисляем доступное время для текущего исполнителя
                available_time = schedule_duration - executor_time_used[executor_index]

                # Определяем, сколько времени займет задача (полностью или частично)
                time_to_assign = min(remaining_duration, available_time)

                # Создаем ScheduleItem для задачи или ее части
                self.__executor_schedule[executor_index].append(
                    ScheduleItem(task, executor_time_used[executor_index], time_to_assign,
                                 is_downtime=False if task else True))

                # Обновляем использованное время исполнителя и оставшееся время задачи
                executor_time_used[executor_index] += time_to_assign
                remaining_duration -= time_to_assign

                # Если задача полностью выполнена, убираем ее из очереди
                if remaining_duration <= 0:
                    task_queue.pop(0)
                else:
                    # Иначе  обновляем оставшееся время задачи в очереди для следующего исполнителя
                    task_queue[0] = (task, remaining_duration)

        # Добавляем время простоя, если необходимо
        for i, executor_schedule in enumerate(self.__executor_schedule):
            if executor_time_used[i] < schedule_duration:
                downtime = schedule_duration - executor_time_used[i]
                executor_schedule.append(ScheduleItem(None, executor_time_used[i], downtime, is_downtime=True))
    @staticmethod
    def __validate_params(tasks: list[Task]) -> None:
        """Проводит валидацию входящих параметров для инициализации объекта
        класса Schedule."""
        if not isinstance(tasks, list):
            raise ScheduleArgumentError(ERR_TASKS_NOT_LIST_MSG)
        if len(tasks) < 1:
            raise ScheduleArgumentError(ERR_TASKS_EMPTY_LIST_MSG)
        for idx, value in enumerate(tasks):
            if not isinstance(value, Task):
                raise ScheduleArgumentError(ERR_INVALID_TASK_TEMPL.format(idx))

    def __validate_executor_idx(self, executor_idx: int) -> None:
        """Проводит валидацию индекса исполнителя."""
        if not isinstance(executor_idx, int) or executor_idx < 0:
            raise ScheduleArgumentError(ERR_EXECUTOR_NOT_INT_MSG)
        if executor_idx >= self.executor_count:
            raise ScheduleArgumentError(ERR_EXECUTOR_OUT_OF_RANGE_MSG)


if __name__ == '__main__':
    print('Пример использования класса Schedule')

    # Инициализируем входные данные для составления расписания
    tasks = [Task('a', 3), Task('b', 4), Task('c', 6), Task('d', 7),
             Task('e', 7), Task('f', 9), Task('g', 10), Task('h', 12),
             Task('i', 17)]

    # Инициализируем экземпляр класса Schedule
    # при этом будет рассчитано расписание для каждого исполнителя
    schedule = Schedule(tasks, 5)

    # Выведем в консоль полученное расписание
    print(schedule)
    for i in range(schedule.executor_count):
        print(f'\nРасписание для исполнителя # {i + 1}:')
        for schedule_item in schedule.get_schedule_for_executor(i):
            print(schedule_item)
