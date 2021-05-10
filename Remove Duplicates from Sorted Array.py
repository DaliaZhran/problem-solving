# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.

"""
from typing import List

# approach 1: popping duplicates from list -> O(n^2)

# approach 2: Two pointers
# time: O(n)
# space: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[i - count] = nums[i]
            else:
                count += 1
        return n - count


# general sol -> counting our unique numbers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        count = k
        for i in range(k, len(nums)):
            if nums[count - k] != nums[i]:  # we compare current number with numbers in our new list
                nums[count] = nums[i]
                count += 1
        return count
