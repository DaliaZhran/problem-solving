# https://leetcode.com/problems/reverse-pairs/

"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
"""

# Approach 1: Brute Force [Time Limit Exceeded]
# Time: O(N^2)
# Space: O(1)
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > 2 * nums[j]:
                    count += 1
        return count
