"""Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length."""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == val:
                nums[i] = nums[j]
                j += 1
            else:
                i += 1
                j+=1
        return i+1


nums = [3, 2, 2, 3]
value = 3
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
obj = Solution()
obj.removeElement(nums, value)
print(obj.removeElement(nums2, val2))
print(nums)
print(nums2)
