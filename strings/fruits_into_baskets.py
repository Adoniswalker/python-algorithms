# https://www.educative.io/courses/grokking-the-coding-interview/Bn2KLlOR0lQ
import unittest


def solution(fruits):
    left = 0
    max_l = -1
    d = {}
    for right in range(len(fruits)):
        right_c = fruits[right]
        d[right_c] = 1 if right_c not in d else d[right_c] + 1
        while len(d) > 2:
            left_c = fruits[left]
            d[left_c] -= 1
            if d[left_c] == 0:
                del d[left_c]
            left += 1
        max_l = max(max_l, right - left + 1)
    return max_l


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(['A', 'B', 'C', 'A', 'C']), 3)
        self.assertEqual(solution(['A', 'B', 'C', 'B', 'B', 'C']), 5)

