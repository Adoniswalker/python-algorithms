import unittest


def solution(data):
    data.sort()


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual([6, 2, 4, 10], 'data')
