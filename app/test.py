"""
All needed tests for sum, mult, min, max,
where values are equivalent, monotonic and two types.
"""

import unittest
import app.main as m


class MinimumTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(m._min([i for i in range(1, 10)]) == 1)

    def test_2(self):
        self.assertTrue(m._min([i for i in range(-10, 1)]) == -10)

    def test_3(self):
        self.assertTrue(m._min([0, 0, 0, 0]) == 0)

    def test_4(self):
        self.assertTrue(m._min([1, -1, 1, -1, 1, -1]) == -1)


class MaximumTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(m._max([i for i in range(1, 10)]) == 9)

    def test_2(self):
        self.assertTrue(m._max([i for i in range(-10, 1)]) == 0)

    def test_3(self):
        self.assertTrue(m._max([0, 0, 0, 0]) == 0)

    def test_4(self):
        self.assertTrue(m._max([1, -1, 1, -1, 1, -1]) == 1)


class SummaTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(m._sum([i for i in range(1, 10)]) == 45)

    def test_2(self):
        self.assertTrue(m._sum([i for i in range(-10, 1)]) == -55)

    def test_3(self):
        self.assertTrue(m._sum([0, 0, 0, 0]) == 0)

    def test_4(self):
        self.assertTrue(m._sum([1, -1, 1, -1, 1, -1]) == 0)


class MultiplicationTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(m._mult([i for i in range(1, 10)]) == 362880)

    def test_2(self):
        self.assertTrue(m._mult([i for i in range(-10, 1)]) == 0)

    def test_3(self):
        self.assertTrue(m._mult([0, 0, 0, 0]) == 0)

    def test_4(self):
        self.assertTrue(m._mult([1, -1, 1, -1, 1, -1]) == -1)


class ReadTest(unittest.TestCase):
    def test(self):
        self.assertTrue(
            m._read("./app/tests/test_el_read.txt") == [1, 2, 3, 4, 0, 0, -1, -1]
        )


if __name__ == "__main__":
    unittest.main()
