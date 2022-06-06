# https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
import unittest


def longest_substring_with_k_unique_characters(arr, k):
    left = 0
    large = []
    max_l = 0
    d = {}
    for right in range(len(arr)):
        right_c = arr[right]
        d[right_c] = 1 if right_c not in d else d[right_c]+1
        while len(d) > k:
            left_c = arr[left]
            d[left_c] -= 1
            if d[left_c] == 0:
                del d[left_c]
            left += 1
        if right-left+1 > max_l:
            large = [left, right+1]
            print(arr[left:right+1])
            max_l = right-left+1
    return arr[large[0]:large[1]]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertIn(longest_substring_with_k_unique_characters("aabbcc", 1), {"aa" , "bb" , "cc"})
        # self.assertIn(longest_substring_with_k_unique_characters("aabbcc", 2), {"aabb" , "bbcc"})
        # self.assertIn(longest_substring_with_k_unique_characters("aabbcc", 3), {"aabbcc" })
        # self.assertIn(longest_substring_with_k_unique_characters("aaabbb", 3), {None})
