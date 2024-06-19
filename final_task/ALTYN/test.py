import unittest
from main import dijkstra
class TestDijkstra(unittest.TestCase):
    """Это будет класс для тестирования разработанного алгоритма"""

    def test_small_graph(self):
        """Тест для небольшого графа"""
        graph = {
            0: [(1, 4), (2, 1)],
            1: [(3, 1)],
            2: [(1, 2), (3, 5)],
            3: [(4, 3)],
            4: []
        }
        start_vertex = 0
        expected_distances = [0, 3, 1, 4, 7]
        self.assertEqual(dijkstra(graph, start_vertex), expected_distances)

    def test_disconnected_graph(self):
        """Тест для графа с несвязанными вершинами"""
        graph = {
            0: [(1, 4)],
            1: [(2, 6)],
            2: [],
            3: [],
            4: []
        }
        start_vertex = 0
        expected_distances = [0, 4, 10, float('inf'), float('inf')]
        self.assertEqual(dijkstra(graph, start_vertex), expected_distances)

    def test_large_graph(self):
        """Тест для большого графа"""
        graph = {
            0: [(1, 4), (2, 1)],
            1: [(3, 1)],
            2: [(1, 2), (3, 5)],
            3: [(4, 3)],
            4: [],
            5: [(6, 2)],
            6: [(7, 3)],
            7: [(8, 4)],
            8: [(9, 5)],
            9: []
        }
        start_vertex = 0
        expected_distances = [0, 3, 1, 4, 7, float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
        self.assertEqual(dijkstra(graph, start_vertex), expected_distances)


if __name__ == '__main__':
    unittest.main()