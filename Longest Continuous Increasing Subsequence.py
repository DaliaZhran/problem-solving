# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

"""
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
"""

# Approach 1; burte force O(N^2)


# Sliding Window
# Time: O(n)
# Space: O(1)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 0
        start = 0
        for end in range(len(nums)):
            if end > 0 and nums[end - 1] >= nums[end]:
                start = end
            result = max(result, end - start + 1)
        return result


# DP
# Time: O(n)
# Space: O(n)
class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)
