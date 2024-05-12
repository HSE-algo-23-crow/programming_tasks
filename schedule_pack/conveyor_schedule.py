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
        """Процедура составляет расписание из элементов ScheduleItem для каждого
               исполнителя, согласно алгоритму Джонсона.

               Parameters:
               tasks (List[Task]): Список задач для расписания.

               Returns:
               List[List[ScheduleItem]]: Расписание для каждого исполнителя.
               """
        self._executor_schedule[0].append(
            ScheduleItem(task=None, start=0, duration=tasks[0].stage_durations[0], is_downtime=True))
        self._executor_schedule[1].append(ScheduleItem(task=tasks[0], start=0, duration=tasks[0].stage_durations[0]))

        self._executor_schedule[0].append(
            ScheduleItem(start=self._executor_schedule[1][0].end, duration=tasks[0].stage_durations[1], task=tasks[0]))

        for task in tasks[1:]:
            schedule_item_1 = ScheduleItem(start=self._executor_schedule[1][-1].end, duration=task.stage_durations[0],
                                           task=task)
            self._executor_schedule[1].append(schedule_item_1)
            last_executor_schedule_1_end = self._executor_schedule[1][-1].end
            last_executor_schedule_0_end = self._executor_schedule[0][-1].end

            if last_executor_schedule_1_end > last_executor_schedule_0_end:
                start = last_executor_schedule_1_end
                duration = last_executor_schedule_1_end - last_executor_schedule_0_end
            else:
                start = last_executor_schedule_0_end
                duration = last_executor_schedule_0_end - last_executor_schedule_1_end

            schedule_item_0 = ScheduleItem(task=None, start=start, duration=duration, is_downtime=True)
            self._executor_schedule[0].append(schedule_item_0)

            schedule_item_2 = ScheduleItem(start=start, duration=task.stage_durations[1], task=task)
            self._executor_schedule[0].append(schedule_item_2)

        self._executor_schedule[1].append(ScheduleItem(task=None, start=self._executor_schedule[1][-1].end,
                                                       duration=self._executor_schedule[0][-1].end -
                                                                self._executor_schedule[1][-1].end,
                                                       is_downtime=True))

        self._executor_schedule[0], self._executor_schedule[1] = self._executor_schedule[1], self._executor_schedule[0]

    @staticmethod
    def __sort_tasks(tasks: list[StagedTask]) -> list[StagedTask]:
        """Возвращает отсортированный список задач для применения
        алгоритма Джонсона."""
        stage1_tasks: list[StagedTask] = []
        stage2_tasks: list[StagedTask] = []

        [stage1_tasks.append(task) if task.stage_duration(0) <= task.stage_duration(1) else stage2_tasks.append(task) for task in tasks]

        stage1_tasks.sort(key=lambda task: task.stage_duration(0))
        stage2_tasks.sort(key=lambda task: task.stage_duration(1), reverse=True)
        print([stage.name for stage in stage1_tasks],[stage.name for stage in stage2_tasks])



        return stage1_tasks + stage2_tasks

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
