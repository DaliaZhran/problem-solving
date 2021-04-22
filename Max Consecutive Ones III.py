# https://leetcode.com/problems/max-consecutive-ones-iii/

"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""

# Sliding Window
# Time: O(N)
# Space: O(1)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = max_len = start = 0

        for end, end_val in enumerate(nums):
            zeros += 1 - end_val
            while zeros > k:
                zeros -= 1 - nums[start]
                start += 1
            max_len = max(max_len, end - start + 1)

        return max_len
