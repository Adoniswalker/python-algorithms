# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and
# returns the new length. Do not allocate extra space for another array, you must do this by modifying the input
# array in-place with O(1) extra memory.
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 1
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            right +=1
        return left +1


if __name__ == '__main__':
    obj = Solution()
    l1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    l1_ans = [0, 1, 2, 3, 4]
    l2 = [1, 1, 2]
    l2_ans = [1, 2]
    print(obj.removeDuplicates(l2))
    print(obj.removeDuplicates(l1))
    print(obj.removeDuplicates([1,1]))
    print(l2)
    print(l1)
