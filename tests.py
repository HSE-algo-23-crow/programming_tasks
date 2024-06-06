import unittest

from main import encode, decode, ERR_NOT_LIST_MSG, ERR_NOT_INT_TEMPL, \
    ERR_EMPTY_LIST_MSG, ERR_NOT_START_WITH_0_MSG, ERR_HAS_DUPLICATES_MSG, \
    ERR_OVER_CONSTRAINT_TEMPL


class TestEncode(unittest.TestCase):
    def test_not_list_numbers(self):
        """Проверяет выброс исключения при передаче некорректного списка."""
        incorrect_values = [None, 1, 'str', {'key': 'val'}]
        for val in incorrect_values:
            with self.assertRaises(TypeError) as error:
                encode(val)
            self.assertEqual(ERR_NOT_LIST_MSG, str(error.exception))

    def test_not_list_val(self):
        """Проверяет выброс исключения при передаче некорректного значения
        в списке."""
        incorrect_lists = [[None], [0.1, 0], ['str', 0, 1],
                           [{'key': 'val'}, 0]]
        for lst in incorrect_lists:
            with self.assertRaises(TypeError) as error:
                encode(lst)
            self.assertEqual(ERR_NOT_INT_TEMPL.format(lst[0]),
                             str(error.exception))

    def test_not_start_with_1(self):
        """Проверяет выброс исключения при передаче списка не начинающегося
        с единицы."""
        with self.assertRaises(ValueError) as error:
            encode([1, 0, 2])
        self.assertEqual(ERR_NOT_START_WITH_0_MSG, str(error.exception))

    def test_has_duplicates(self):
        """Проверяет выброс исключения при передаче списка содержащего
        дубликаты."""
        with self.assertRaises(ValueError) as error:
            encode([0, 1, 2, 1])
        self.assertEqual(ERR_HAS_DUPLICATES_MSG, str(error.exception))

    def test_empty_list(self):
        """Проверяет выброс исключения при передаче пустого списка."""
        with self.assertRaises(ValueError) as error:
            encode([])
        self.assertEqual(ERR_EMPTY_LIST_MSG, str(error.exception))

    def test_1(self):
        """Проверка кодировки 1 элемента."""
        self.assertEqual([0], encode([0]))

    def test_2(self):
        """Проверка кодировки 2 элементов."""
        self.assertEqual([0, 0], encode([0, 1]))

    def test_3(self):
        """Проверка кодировки 3 элементов."""
        self.assertEqual([0, 1, 0], encode([0, 2, 1]))

    def test_4(self):
        """Проверка кодировки 4 элементов."""
        self.assertEqual([0, 1, 0, 0], encode([0, 2, 1, 3]))

    def test_5_asc(self):
        """Проверка кодировки 5 элементов, отсортированных по возрастанию."""
        self.assertEqual([0, 0, 0, 0, 0], encode([0, 1, 2, 3, 4]))

    def test_6_desc(self):
        """Проверка кодировки 6 элементов, отсортированных по убыванию."""
        self.assertEqual([0, 4, 3, 2, 1, 0], encode([0, 5, 4, 3, 2, 1]))

    def test_20(self):
        """Проверка кодировки 20 элементов."""
        natural = [0, 17, 4, 18, 6, 15, 16, 11, 9, 12, 13, 10, 8, 14, 5, 3,
                   19, 7, 1, 2]
        alter = [0, 16, 3, 15, 4, 12, 12, 8, 6, 7, 7, 6, 5, 5, 3, 2, 3, 2, 0,
                 0]
        self.assertEqual(alter, encode(natural))


class TestDecode(unittest.TestCase):
    def test_not_list_numbers(self):
        """Проверяет выброс исключения при передаче некорректного списка."""
        incorrect_values = [None, 1, 'str', {'key': 'val'}]
        for val in incorrect_values:
            with self.assertRaises(TypeError) as error:
                decode(val)
            self.assertEqual(ERR_NOT_LIST_MSG, str(error.exception))

    def test_not_list_val(self):
        """Проверяет выброс исключения при передаче некорректного значения
        в списке."""
        incorrect_lists = [[None], [0.1, 0], ['str', 0, 1],
                           [{'key': 'val'}, 0]]
        for lst in incorrect_lists:
            with self.assertRaises(TypeError) as error:
                decode(lst)
            self.assertEqual(ERR_NOT_INT_TEMPL.format(lst[0]),
                             str(error.exception))

        def test_not_start_with_1(self):
            """Проверяет выброс исключения при передаче списка не начинающегося
            с единицы."""
            with self.assertRaises(ValueError) as error:
                decode([1, 0, 2])
            self.assertEqual(ERR_NOT_START_WITH_0_MSG, str(error.exception))

        def test_empty_list(self):
            """Проверяет выброс исключения при передаче пустого списка."""
            with self.assertRaises(ValueError) as error:
                decode([])
            self.assertEqual(ERR_EMPTY_LIST_MSG, str(error.exception))

        def test_over_constraint(self):
            """Проверяет выброс исключения при передаче пустого списка."""
            with self.assertRaises(ValueError) as error:
                decode([0, 1])
            self.assertEqual(ERR_OVER_CONSTRAINT_TEMPL.format(1, 1), str(error.exception))

        def test_1(self):
            """Проверка декодирования 1 элемента."""
            self.assertEqual([0], decode([0]))

        def test_2(self):
            """Проверка декодирования 2 элементов."""
            self.assertEqual([0, 1], decode([0, 0]))

        def test_3(self):
            """Проверка декодирования 3 элементов."""
            self.assertEqual([0, 2, 1], decode([0, 1, 0]))

        def test_4(self):
            """Проверка декодирования 4 элементов."""
            self.assertEqual([0, 2, 1, 3], decode([0, 1, 0, 0]))

        def test_5_asc(self):
            """Проверка декодирования 5 элементов, отсортированных по возрастанию."""
            self.assertEqual([0, 1, 2, 3, 4], decode([0, 0, 0, 0, 0]))

        def test_6_desc(self):
            """Проверка декодирования 6 элементов, отсортированных по убыванию."""
            self.assertEqual([0, 5, 4, 3, 2, 1], decode([0, 4, 3, 2, 1, 0]))

        def test_20(self):
            """Проверка декодирования 20 элементов."""
            natural = [0, 17, 4, 18, 6, 15, 16, 11, 9, 12, 13, 10, 8, 14, 5, 3,
                       19, 7, 1, 2]
            alter = [0, 16, 3, 15, 4, 12, 12, 8, 6, 7, 7, 6, 5, 5, 3, 2, 3, 2, 0,
                     0]
            self.assertEqual(natural, decode(alter))

    if __name__ == '__main__':
        unittest.main()