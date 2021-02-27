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


# Time: O(n)
# Space: O(n)
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        max_size = 0
        curr_sum = 0
        acc_sums = {}

        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum not in acc_sums:  # we want the furthest sum on the left to increase size
                acc_sums[curr_sum] = i
            if curr_sum == k:
                max_size = i + 1
            elif curr_sum - k in acc_sums:
                max_size = max(max_size, i - acc_sums[curr_sum - k])  # sum[j] - sum[i] = k -> sum[j] - k = sum[i]

        return max_size


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        answer = 0
        curr_sum = 0
        prev_sums = {0: -1}  # if sum == k, return -1 to just add 1 to the current index
        for idx, val in enumerate(nums):
            curr_sum += val
            if curr_sum not in prev_sums:
                prev_sums[curr_sum] = idx
            # if curr_sum == k:
            #     answer = max(answer, idx + 1)
            if curr_sum - k in prev_sums:
                answer = max(answer, idx - prev_sums[curr_sum - k])

        return answer
