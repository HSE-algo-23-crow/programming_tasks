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
        self._executor_schedule[1].append(ScheduleItem(task=tasks[0], start=0, duration=tasks[0].stage_durations[0]))
        self._executor_schedule[0].append(ScheduleItem(task=None ,start=0, duration=tasks[0].stage_durations[0],
                                                       is_downtime=True))
        self._executor_schedule[0].append(ScheduleItem(start=self._executor_schedule[1][0].end,
                    duration=tasks[0].stage_durations[1], task=tasks[0]))
        for i in tasks[1:]:
            self._executor_schedule[1].append(ScheduleItem(start=self._executor_schedule[1][-1].end,
                                                           duration=i.stage_durations[0], task=i))
            start = max(self._executor_schedule[1][-1].end, self._executor_schedule[0][-1].end)
            self._executor_schedule[0].append(ScheduleItem(start=start, duration=i.stage_durations[1], task=i))
        self._executor_schedule[0].append(ScheduleItem(task=None, start = self._executor_schedule[1][-1].end,
                                                       duration= self._executor_schedule[0][-1].end-
                                                                 self._executor_schedule[1][-1].end,
                                                       is_downtime=True))

    @staticmethod
    def __sort_tasks(tasks: list[StagedTask]) -> list[StagedTask]:
        part1 = []
        part2 = []
        for i in tasks:
            if i.stage_durations[0] < i.stage_durations[1]:
                flag = True
                for j in range(len(part1)):
                    if (part1[j].stage_durations[0] > i.stage_durations[0]):
                        part1.insert(j, i)
                        flag = False
                        break
                if flag: part1.append(i)
            else:
                flag = True
                for j in range(len(part2)):
                    if (part2[j].stage_durations[1] < i.stage_durations[1]):
                        part2.insert(j, i)
                        flag = False
                        break
                if flag: part2.append(i)
        return part1 + part2

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
        StagedTask('a', [4, 3]),
        StagedTask('b', [5, 2]),
        StagedTask('c', [3, 5]),
        StagedTask('d', [2, 3]),
        StagedTask('e', [4, 4])
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
