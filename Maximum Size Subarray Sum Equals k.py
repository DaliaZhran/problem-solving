# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:
"""


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        answer = 0
        curr_sum = 0
        prev_sums = defaultdict(int)
        for right, val in enumerate(nums):
            curr_sum += val
            if curr_sum not in prev_sums:
                prev_sums[curr_sum] = right
            if curr_sum == k:
                answer = max(answer, right + 1)
            elif curr_sum - k in prev_sums:
                answer = max(answer, right - prev_sums[curr_sum - k])

        return answer


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        answer = 0
        curr_sum = 0
        # prev_sums = defaultdict(int)
        prev_sums = {0: -1}  # if sum == k, return -1 to add 1 to the right
        for right, val in enumerate(nums):
            curr_sum += val
            if curr_sum not in prev_sums:
                prev_sums[curr_sum] = right
            # if curr_sum == k:
            #     answer = max(answer, right + 1)
            if curr_sum - k in prev_sums:
                answer = max(answer, right - prev_sums[curr_sum - k])

        return answer
