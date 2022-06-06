# Maximum Sum Subarray of Size K
# https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP
import unittest


def max_sub_array_of_size_k_option_1(k, arr):
    max_sum = 0
    for pos in range(len(arr)-k+1):
        t = 0
        for p in range(pos, pos + k):
            t += arr[p]
        if t > max_sum:
            max_sum = t
    return max_sum


def max_sub_array_of_size_k_option_2(k, arr):
    max_s, start, win_sum = 0,0,0
    for end in range(len(arr)):
        win_sum += arr[end]
        if end >= k-1:
            max_s = max(win_sum, max_s)
            win_sum -= arr[start]
            start += 1
    return max_s



class TestSolution(unittest.TestCase):
    def test_solution_1(self):
        self.assertEqual(max_sub_array_of_size_k_option_1(3, [2, 1, 5, 1, 9, 9]), 19)
        self.assertEqual(max_sub_array_of_size_k_option_1(2, [2, 3, 4, 1, 5]), 7)

    def test_solution_2(self):
        self.assertEqual(max_sub_array_of_size_k_option_2(3, [2, 1, 5, 1, 9, 9]), 19)
        self.assertEqual(max_sub_array_of_size_k_option_2(2, [2, 3, 4, 1, 5]), 7)
