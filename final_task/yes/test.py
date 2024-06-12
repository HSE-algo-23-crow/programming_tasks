import unittest
from main import check_params, check_path, check_distance, run
from final_task.yes.errors.ers import (ALPHA_VALUE_ERROR, BETA_VALUE_ERROR, ALPHA_BETA_ZERO_ERROR, VAPORIZE_VALUE_ERROR,
                                       CITIES_NUMBER_ERROR, Q_VALUE_ERROR,
                                       ITERATIONS_NUMBER_ERROR, DISTANCE_NEGATIVE_ERROR,
                                       PATH_NOT_FOUND_ERROR)
from final_task.yes.Structure.paths import Paths


class Test_ant_algorithm_params(unittest.TestCase):
    """Это будет класс для тестирования разработанного алгоритма (всяческие принимаемые значения)"""

    def test_alpha_value(self):
        """Проверяет гиперпараметр альфа"""
        with self.assertRaises(ValueError) as error:
            check_params(-1, 1, 0.9, 1, 2, 1)
        self.assertEqual(ALPHA_VALUE_ERROR.format(-1), str(error.exception))

    def test_beta_value(self):
        """Проверяет гиперпараметр бета"""
        with self.assertRaises(ValueError) as error:
            check_params(1, -1, 0.9, 1, 2, 1)
        self.assertEqual(BETA_VALUE_ERROR.format(-1), str(error.exception))

    def test_alpha_beta_zero(self):
        """Проверяет гиперпараметр бета"""
        with self.assertRaises(ValueError) as error:
            check_params(0, 0, 0.9, 1, 2, 1)
        self.assertEqual(ALPHA_BETA_ZERO_ERROR, str(error.exception))

    def test_alpha_beta_zero(self):
        """Проверяет гиперпараметр бета"""
        with self.assertRaises(ValueError) as error:
            check_params(0, 0, 0.9, 1, 2, 1)
        self.assertEqual(ALPHA_BETA_ZERO_ERROR, str(error.exception))

    def test_vaporize_value_1(self):
        """Проверяет значение испарение феромона 1"""
        with self.assertRaises(ValueError) as error:
            check_params(1, 1, 1.1, 1, 2, 1)
        self.assertEqual(VAPORIZE_VALUE_ERROR.format(1.1), str(error.exception))

    def test_vaporize_value_2(self):
        """Проверяет значение испарение феромона 2"""
        with self.assertRaises(ValueError) as error:
            check_params(1, 1, -0.1, 1, 2, 1)
        self.assertEqual(VAPORIZE_VALUE_ERROR.format(-0.1), str(error.exception))

    def test_q_value(self):
        """Проверяет гиперпараметр количества феромона на муравья"""
        with self.assertRaises(ValueError) as error:
            check_params(1, 1, 0.9, -1, 2, 1)
        self.assertEqual(Q_VALUE_ERROR.format(-1), str(error.exception))

    def test_n_value(self):
        """Проверяет гиперпараметр количество точек"""
        with self.assertRaises(ValueError) as error:
            check_params(1, 1, 0.9, 1, 1, 1)
        self.assertEqual(CITIES_NUMBER_ERROR.format(1), str(error.exception))

    def test_it_value(self):
        """Проверяет гиперпараметр количество итераций"""
        with self.assertRaises(ValueError) as error:
            check_params(1, 1, 0.9, 1, 2, -1)
        self.assertEqual(ITERATIONS_NUMBER_ERROR.format(-1), str(error.exception))

    def test_distance_value(self):
        """Проверяет дистанцию между двумя точками"""
        with self.assertRaises(ValueError) as error:
            check_distance(-1)
        self.assertEqual(DISTANCE_NEGATIVE_ERROR.format(-1), str(error.exception))

    def test_paths(self):
        """Проверяет есть ли путь"""
        with self.assertRaises(UserWarning) as error:
            p = Paths(1.0, 1.0)
            p.set_paths([[[None, 1], [float('inf'), 1], [float('inf'), 1]], [[1, 1], [None, 1], [1, 1]], [[1, 1], [1, 1], [None, 1]]])
            p.names = ['a', 'b', 'c']
            check_path(p)
        self.assertEqual(PATH_NOT_FOUND_ERROR, str(error.exception))


class Test_ant_algorithm(unittest.TestCase):
    """Это будет класс для тестирования разработанного алгоритма"""

    def test_res_1(self):
        """Проверяет результат работы алгоритма 1"""
        p = Paths(1, 1)
        p.length = 3
        p.names = ['a', 'b', 'c']
        p.set_names({'a': 0, 'b': 1, 'c': 2})
        p.set_paths([[[None, 1], [13, 1], [54, 1]], [[21, 1], [None, 1], [9, 1]], [[107, 1], [18, 1], [None, 1]]])

        res = run(0.9, 4, 3, 5, p)
        self.assertTrue(any([i[1] == 93 for i in res]))


    def test_res_2(self):
        """Проверяет результат работы алгоритма 2"""
        p = Paths(1, 1)
        p.length = 3
        p.names = ['a', 'b', 'c']
        p.set_names({'a': 0, 'b': 1, 'c': 2})
        p.set_paths([[[None, 1], [1, 1], [2, 1]], [[3, 1], [None, 1], [4, 1]], [[5, 1], [6, 1], [None, 1]]])

        res = run(0.9, 4, 3, 5, p)
        self.assertTrue(any([i[1] == 10 for i in res]))


if __name__ == '__main__':
    unittest.main()
