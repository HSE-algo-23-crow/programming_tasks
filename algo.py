import random
import unittest

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

class TestQuicksort(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(quicksort([]), [])

    def test_single_element_array(self):
        self.assertEqual(quicksort([1]), [1])

    def test_all_elements_same(self):
        self.assertEqual(quicksort([1, 1, 1]), [1, 1, 1])

    def test_sorted_array(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(quicksort([-1, -3, -2, 0, 2, 1]), [-3, -2, -1, 0, 1, 2])

    def test_repeating_elements(self):
        self.assertEqual(quicksort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_floating_point_numbers(self):
        self.assertEqual(quicksort([3.1, 2.4, 5.6, 1.2, 3.3]), [1.2, 2.4, 3.1, 3.3, 5.6])

    def test_random_array(self):
        arr = [random.randint(1, 1000) for _ in range(1000)]
        self.assertEqual(quicksort(arr), sorted(arr))

if __name__ == "__main__":
    unittest.main()
