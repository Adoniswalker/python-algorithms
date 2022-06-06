# https://www.educative.io/courses/grokking-the-coding-interview/YQQwQMWLx80
import unittest


def longest_substring_with_k_distinct(str1, k):
    h = {}
    start, max_l = 0, 0
    for end in range(len(str1)):
        end_c = str1[end]
        if end_c not in h:
            h[end_c] = 0
        h[end_c] += 1
        while len(h) > k:
            start_c = str1[start]
            h[start_c] -= 1
            if h[start_c] == 0:
                del h[start_c]
            start += 1
        max_l = max(max_l, end-start+1)
    return max_l


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(longest_substring_with_k_distinct("araaci", 2), 4)
        # self.assertEqual(longest_substring_with_k_distinct("araaci", 1), 2)
        # self.assertEqual(longest_substring_with_k_distinct("cbbebi", 3), 5)
        # self.assertEqual(longest_substring_with_k_distinct("cbbebi", 10), 6)
