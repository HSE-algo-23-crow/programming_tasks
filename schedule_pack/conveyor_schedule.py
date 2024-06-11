from schedule_pack.abs_schedule import AbstractSchedule
from schedule_pack.errors import ScheduleArgumentError
from schedule_pack.staged_task import StagedTask
from schedule_pack.schedule_item import ScheduleItem
from schedule_pack.constants import ERR_TASKS_NOT_LIST_MSG, \
    ERR_TASKS_EMPTY_LIST_MSG, ERR_INVALID_TASK_TEMPL, \
    ERR_INVALID_STAGE_CNT_TEMPL


class ConveyorSchedule(AbstractSchedule):
    """Класс представляет оптимальное расписание для списка задач, состоящих
     из двух этапов и двух исполнителей. Для построения расписания используется
     алгоритм Джонсона.

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

    def __init__(self, tasks: list[StagedTask]):
        """Конструктор для инициализации объекта расписания.

        :param tasks: Список задач для составления расписания.
        :raise ScheduleArgumentError: Если список задач предоставлен в
        некорректном формате или количество этапов для какой-либо задачи не
        равно двум.
        """
        ConveyorSchedule.__validate_params(tasks)
        super().__init__(tasks, 2)

        # Процедура заполняет пустую заготовку расписания для каждого
        # исполнителя объектами ScheduleItem.
        self.__fill_schedule(ConveyorSchedule.__sort_tasks(tasks))

    @property
    def duration(self) -> float:
        """Возвращает общую продолжительность расписания."""
        return self._executor_schedule[0][-1].end

    def __fill_schedule(self, tasks: list[StagedTask]) -> None:
        """Процедура составляет расписание из элементов ScheduleItem для каждого
        исполнителя, согласно алгоритму Джонсона."""
        first_executor = []
        first_current = 0

        second_executor = []
        second_current = 0

        for index in range(len(tasks) + 1):
            if index == 0:

                first_executor.append(ScheduleItem(tasks[index], 0, tasks[index].stage_durations[0]))
                second_executor.append(ScheduleItem(None, 0, tasks[index].stage_durations[0], is_downtime=True))

                first_current += tasks[index].stage_durations[0]
                second_current += tasks[index].stage_durations[0]

            else:
                time_gap = first_current - second_current
                if second_current < first_current:
                    second_executor.append(ScheduleItem(None, second_current, time_gap, is_downtime=True))
                    second_current = first_current

                prev = index - 1

                second_executor.append(ScheduleItem(tasks[prev], second_current, tasks[prev].stage_durations[1]))
                second_current += tasks[prev].stage_durations[1]

                if index != len(tasks):
                    first_executor.append(ScheduleItem(tasks[index], first_current, tasks[index].stage_durations[0]))
                    first_current += tasks[index].stage_durations[0]

        remaining_gap = second_current - first_current

        if (first_current < second_current):
            first_executor.append(ScheduleItem(None, first_current, remaining_gap, is_downtime=True))

        self._executor_schedule = [first_executor, second_executor]

    @staticmethod
    def __sort_tasks(tasks: list[StagedTask]) -> list[StagedTask]:
        """Возвращает отсортированный список задач для применения
        алгоритма Джонсона."""
        first_set = []
        second_set = []
        for task in tasks:
            if task.stage_duration(0) <= task.stage_duration(1):
                first_set.append(task)
            else:
                second_set.append(task)
        first_set.sort(key=lambda duration: duration.stage_duration(0))
        second_set.sort(key=lambda duration: duration.stage_duration(1), reverse=True)
        sorted_tasks = first_set + second_set
        return sorted_tasks

    @staticmethod
    def __validate_params(tasks: list[StagedTask]) -> None:
        """Проводит валидацию входящих параметров для инициализации объекта
        класса ConveyorSchedule."""
        if not isinstance(tasks, list):
            raise ScheduleArgumentError(ERR_TASKS_NOT_LIST_MSG)
        if len(tasks) < 1:
            raise ScheduleArgumentError(ERR_TASKS_EMPTY_LIST_MSG)
        for idx, value in enumerate(tasks):
            if not isinstance(value, StagedTask):
                raise ScheduleArgumentError(ERR_INVALID_TASK_TEMPL.format(idx))
            if value.stage_count != 2:
                raise ScheduleArgumentError(
                    ERR_INVALID_STAGE_CNT_TEMPL.format(idx))


if __name__ == '__main__':
    print('Пример использования класса ConveyorSchedule')

    # Инициализируем входные данные для составления расписания
    tasks = [
        StagedTask('a', [7, 2]),
        StagedTask('b', [3, 4]),
        StagedTask('c', [2, 5]),
        StagedTask('d', [4, 1]),
        StagedTask('e', [6, 6]),
        StagedTask('f', [5, 3]),
        StagedTask('g', [4, 5])
    ]

    # Инициализируем экземпляр класса Schedule
    # при этом будет рассчитано расписание для каждого исполнителя
    schedule = ConveyorSchedule(tasks)

    # Выведем в консоль полученное расписание
    print(schedule)
    for i in range(schedule.executor_count):
        print(f'\nРасписание для исполнителя # {i + 1}:')
        for schedule_item in schedule.get_schedule_for_executor(i):
            print(schedule_item)
