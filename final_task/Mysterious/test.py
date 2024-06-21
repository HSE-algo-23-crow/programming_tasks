import unittest
from main import (substring_search, ERR_EMPTY_BOTH_STRINGS, ERR_EMPTY_INIT_STRING, ERR_EMPTY_SUBSTRING,
                  ERR_SUBSTRING_LARGE_THAN_INIT_STRING)


class TestSubstringSearch(unittest.TestCase):

    def test_1_empty_both_strings(self):
        """Проверяет выброс уникального исключения при пустых начальной строке и подстроке"""
        with self.assertRaises(ValueError) as error:
            substring_search("", "")
        self.assertEqual(ERR_EMPTY_BOTH_STRINGS, str(error.exception))

    def test_2_empty_substring(self):
        """Проверяет выброс исключения при пустой подстроке"""
        with self.assertRaises(ValueError) as error:
            substring_search("", "Бла-бла")
        self.assertEqual(ERR_EMPTY_SUBSTRING, str(error.exception))

    def test_3_empty_init_string(self):
        """Проверяет выброс исключения при пустой начальной строке"""
        with self.assertRaises(ValueError) as error:
            substring_search("Бла", "")
        self.assertEqual(ERR_EMPTY_INIT_STRING, str(error.exception))

    def test_4_substring_large_than_init_string(self):
        """Проверяет выброс исключения, если длина искомой подстроки больше, чем длина начальной строки"""
        with self.assertRaises(ValueError) as error:
            substring_search("Я длиннее начальной строки", "Я - начальная строка")
        self.assertEqual(ERR_SUBSTRING_LARGE_THAN_INIT_STRING, str(error.exception))

    def test_5(self):
        """Проверка поиска при отсутствии искомой подстроки в начальной строке"""
        init_string = "Первая в Европе женщина-офтальмолог родилась в Черновцах."
        substring = "мужчина"
        index = substring_search(substring, init_string)
        self.assertEqual(index, -1)

    def test_6(self):
        """Проверка поиска при отсутствии искомой подстроки в начальной строке"""
        init_string = "Одной из лучших игр эпохи 16-битных консолей считается платформер, рекламирующий McDonald’s."
        substring = "Burger King"
        index = substring_search(substring, init_string)
        self.assertEqual(index, -1)

    def test_7(self):
        """Проверка поиска присутствующей подстроки в строке"""
        init_string = "Первая в Европе женщина-офтальмолог родилась в Черновцах."
        substring = "женщина"
        index = substring_search(substring, init_string)
        self.assertEqual(index, 16)

    def test_8(self):
        """Проверка поиска присутствующей подстроки в строке"""
        init_string = "Одной из лучших игр эпохи 16-битных консолей считается платформер, рекламирующий McDonald’s."
        substring = "лучших игр"
        index = substring_search(substring, init_string)
        self.assertEqual(index, 9)

    def test_9(self):
        """Проверка поиска присутствующей подстроки в строке"""
        init_string = ("История штата Нью-Йорк началась со времени заселения территории штата человеком примерно "
                       "в 10 000 году до н. э.")
        substring = "Нью-Йорк"
        index = substring_search(substring, init_string)
        self.assertEqual(index, 14)


if __name__ == '__main__':
    unittest.main()
