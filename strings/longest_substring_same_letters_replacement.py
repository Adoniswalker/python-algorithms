# Longest Substring with Same Letters after Replacement
import unittest


def length_of_longest_substring(str1, k):
    l, m_c = 0, 0
    for r in range(len(str1)):
        l_c = str1[l]
        r_c = str1[r]
        if l_c != r_c:
            l = r
        m_c = max(m_c, r - l + 1)

    return m_c


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(length_of_longest_substring('aabccbb', 2), 5)
        self.assertEqual(length_of_longest_substring('abbcb', 1), 4)
        self.assertEqual(length_of_longest_substring('abccde', 1), 3)

    def test_longest_unique(self):
        self.assertEqual(length_of_longest_substring('aabccbbb', 2), 3)
        self.assertEqual(length_of_longest_substring('aabccb', 2), 2)
        self.assertEqual(length_of_longest_substring('aabcccbb', 2), 3)
        self.assertEqual(length_of_longest_substring('abcb', 2), 1)
