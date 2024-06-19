import unittest

from main import (DIF_LEN_EXCEPTION, ERROR_TYPE_EXCEPTION, LESS_ZERO,
                  NOT_ORIENTED, ZERO_MATRIX_EXCEPTION, prim_algorythm)


class TestPrimAlgorythm(unittest.TestCase):
    """Класс тестирования разработанного алгоритма Прима"""

    def test_correctness(self):
        """Тест на корректность работы алгоритма Прима"""
        matrix = [
            [0, 19, 5, 0, 0],
            [19, 0, 5, 9, 2],
            [5, 5, 0, 1, 6],
            [0, 9, 1, 0, 1],
            [0, 2, 6, 1, 0],
        ]
        expected_result = [[0, 2, 5], [2, 3, 1], [3, 4, 1], [4, 1, 2]]
        self.assertEqual(prim_algorythm(matrix, 0), expected_result)

    def test_zero_matrix(self):
        """Тест на проверку исключения для пустой матрицы"""
        matrix = []
        with self.assertRaises(Exception) as context:
            prim_algorythm(matrix, 0)
        self.assertTrue(ZERO_MATRIX_EXCEPTION in str(context.exception))

    def test_different_lengths(self):
        """Тест на проверку исключения для матрицы с различным количеством строк и столбцов"""
        matrix = [
            [0, 19, 5],
            [19, 0, 5],
        ]
        with self.assertRaises(Exception) as context:
            prim_algorythm(matrix, 0)
        self.assertTrue(DIF_LEN_EXCEPTION in str(context.exception))

    def test_non_numeric_values(self):
        """Тест на проверку исключения для матрицы с ненумерическими значениями"""
        matrix = [
            [0, 19, 5],
            [19, 0, "a"],
            [5, 5, 0],
        ]
        with self.assertRaises(Exception) as context:
            prim_algorythm(matrix, 0)
        self.assertTrue(ERROR_TYPE_EXCEPTION in str(context.exception))

    def test_negative_weights(self):
        """Тест на проверку исключения для матрицы с отрицательными весами"""
        matrix = [
            [0, 19, 5],
            [19, 0, -5],
            [5, 5, 0],
        ]
        with self.assertRaises(Exception) as context:
            prim_algorythm(matrix, 0)
        self.assertTrue(LESS_ZERO in str(context.exception))

    def test_not_oriented_graph(self):
        """Тест на проверку исключения для неориентированного графа"""
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        with self.assertRaises(Exception) as context:
            prim_algorythm(matrix, 0)
        self.assertTrue(NOT_ORIENTED in str(context.exception))


if __name__ == "__main__":
    unittest.main()
