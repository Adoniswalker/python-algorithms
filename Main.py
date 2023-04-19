from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        items = {}
        for i, value in enumerate(nums):
            complement = items.get(target - value)
            if complement is not None:
                return [complement, i]
            items[value] = i

def find_minimum(num):
    return sorted(num)[0]

if __name__ == '__main__':
    print(find_minimum([9, 2, 3, 6]))
# obj = Solution()
# print(obj.twoSum([2, 7, 7, 11, 15], 9))
