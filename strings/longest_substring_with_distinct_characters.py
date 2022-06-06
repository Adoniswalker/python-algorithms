# Longest Substring with Distinct Characters
# https://www.educative.io/courses/grokking-the-coding-interview/YMzBx1gE5EO
import unittest


def non_repeat_substring(str):
    l, count = 0, 0
    large = ''
    d =set()
    for r in range(len(str)):
        r_c = str[r]
        if r_c in d:
            if r-l+1 > count:
                count = r-l
                large = str[l:r]
                print(large)
            d.clear()
            d.add(r_c)
            l = r
        else:
            d.add(r_c)
    return large


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(non_repeat_substring("aabccbb"), "abc")
        self.assertEqual(non_repeat_substring("abbbb"), "ab")
        self.assertIn(non_repeat_substring("abccde"), {"abc", 'cde'})
