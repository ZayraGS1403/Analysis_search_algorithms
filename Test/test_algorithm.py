import unittest

from Search import algorithms

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target = 10


class test_algorithm(unittest.TestCase):
    def test_lineal_search_true(self):
        self.assertEqual(algorithms.lineal_search(arr, target), True)

    def test_search_in_true(self):
        self.assertEqual(algorithms.search_in(arr, target), True)

    def test_binary_search_true(self):
        self.assertEqual(algorithms.binary_search(arr, target), True)

    def test_ternary_search_true(self):
        self.assertEqual(algorithms.ternary_search(arr, target), True)

    def test_lineal_search_false(self):
        self.assertEqual(algorithms.lineal_search(arr, 21), False)

    def test_search_in_false(self):
        self.assertEqual(algorithms.search_in(arr, 21), False)

    def test_binary_search_false(self):
        self.assertEqual(algorithms.binary_search(arr, 21), False)

    def test_ternary_search_false(self):
        self.assertEqual(algorithms.ternary_search(arr, 21), False)


if __name__ == "__main__":
    unittest.main()
