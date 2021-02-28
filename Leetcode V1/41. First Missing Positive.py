# https://leetcode.com/problems/first-missing-positive/
"""
Given an unsorted integer array nums, find the smallest missing positive integer.

Example 1:

Input: nums = [1,2,0]
Output: 3

Example 2:

Input: nums = [3,4,-1,1]
Output: 2
"""

# normal search -> faster than cyclic sort idk why -> it should be O(n^2) because "in" is O(n)
def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums == []:
        return 1
    for i in range(1, len(nums) + 2):
        if i not in nums:
            return i


# almost same as cyclic sort but with additional space


def firstMissingPositive(self, nums):
    nums_set = set()
    for num in nums:
        if num > 0:
            nums_set.add(num)
    curr = 1
    while curr in nums_set and curr < len(nums) + 1:
        curr += 1
    return curr


# cyclic sort
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        n = len(nums)
        while i < n:
            j = nums[i] - 1
            if j < n and j >= 0 and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
