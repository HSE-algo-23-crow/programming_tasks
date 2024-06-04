import unittest
from main import check_params, check_path, check_distance
from final_task.yes.errors.ers import (ALPHA_VALUE_ERROR, BETA_VALUE_ERROR,
                                       CITIES_NUMBER_ERROR, Q_VALUE_ERROR,
                                       ITERATIONS_NUMBER_ERROR, DISTANCE_NEGATIVE_ERROR,
                                       PATH_NOT_FOUND_ERROR)
from final_task.yes.Structure.paths import Paths


class Test(unittest.TestCase):
    """Это будет класс для тестирования разработанного алгоритма"""

    def test_alpha_value(self):
        """Проверяет гиперпараметр альфа"""
        with self.assertRaises(ValueError) as error:
            check_params(-1, 1, 1, 2, 1)
        self.assertEqual(ALPHA_VALUE_ERROR.format(-1), str(error.exception))

    def test_beta_value(self):
        """Проверяет гиперпараметр бета"""
        with self.assertRaises(ValueError) as error:
            check_params(1, -1, 1, 2, 1)
        self.assertEqual(BETA_VALUE_ERROR.format(-1), str(error.exception))

    def test_q_value(self):
        """Проверяет гиперпараметр количества феромона на муравья"""
        with self.assertRaises(ValueError) as error:
            check_params(1, 1, -1, 2, 1)
        self.assertEqual(Q_VALUE_ERROR.format(-1), str(error.exception))

    def test_n_value(self):
        """Проверяет гиперпараметр количество точек"""
        with self.assertRaises(ValueError) as error:
            check_params(1, 1, 1, 1, 1)
        self.assertEqual(CITIES_NUMBER_ERROR.format(1), str(error.exception))

    def test_it_value(self):
        """Проверяет гиперпараметр количество итераций"""
        with self.assertRaises(ValueError) as error:
            check_params(1, 1, 1, 2, -1)
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


if __name__ == '__main__':
    unittest.main()
