# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3]
Explanation: Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively. It doesn't matter what you leave beyond the returned length.
"""
from typing import List

# approach 1: popping duplicates from list -> O(n^2)

# approach 2: Two pointers
# Time: O(n)
# Space: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2
        count = k
        for i in range(k, len(nums)):
            if nums[count - k] != nums[i]:  # we compare current number with numbers in our new list
                nums[count] = nums[i]
                count += 1
        return count
