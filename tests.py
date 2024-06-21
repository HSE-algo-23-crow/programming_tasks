import random
import unittest
from algo import quicksort
class TestQuicksort(unittest.TestCase):

    # Тест на пустой массив
    def test_empty_array(self):
        self.assertEqual(quicksort([]), [])

    # Тест на массив с одним элементом
    def test_single_element_array(self):
        self.assertEqual(quicksort([1]), [1])

    # Тест на массив, где все элементы одинаковы
    def test_all_elements_same(self):
        self.assertEqual(quicksort([1, 1, 1]), [1, 1, 1])

    # Тест на уже отсортированный массив
    def test_sorted_array(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    # Тест на массив, отсортированный в обратном порядке
    def test_reverse_sorted_array(self):
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    # Тест на массив с отрицательными числами
    def test_negative_numbers(self):
        self.assertEqual(quicksort([-1, -3, -2, 0, 2, 1]), [-3, -2, -1, 0, 1, 2])

    # Тест на массив с повторяющимися элементами
    def test_repeating_elements(self):
        self.assertEqual(quicksort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    # Тест на массив с плавающими числами
    def test_floating_point_numbers(self):
        self.assertEqual(quicksort([3.1, 2.4, 5.6, 1.2, 3.3]), [1.2, 2.4, 3.1, 3.3, 5.6])

    # Тест на случайный массив (проверка на больших массивах)
    def test_random_array(self):
        arr = [random.randint(1, 1000) for _ in range(1000)]
        self.assertEqual(quicksort(arr), sorted(arr))

if __name__ == "__main__":
    unittest.main()
