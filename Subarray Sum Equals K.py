# https://leetcode.com/problems/subarray-sum-equals-k/

"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""


# Brute Force
# Time : O(N^3)
# Space : O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub_arr_sum = 0
                for index in range(i, j):
                    sub_arr_sum += nums[index]
                if sub_arr_sum == k:
                    count += 1
        return count


# Brute Force with Cumulative Sum
# Time : O(N^2)
# Space : O(1)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for start in range(n):
            sub_arr_sum = 0
            for end in range(start, n):
                sub_arr_sum += nums[end]
                if sub_arr_sum == k:
                    count += 1
        return count


# Prefix Sum
# Time : O(N)
# Space : O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        mp = defaultdict(int)
        # add this to count the subarrays == k and starts from the beginning of nums
        mp[0] = 1
        cum_sum = 0
        for i in range(len(nums)):
            # current prefix sum
            cum_sum += nums[i]
            # situation 2 - arrays that do not start from the beginning of nums:
            # number of times the curr_sum − k has occurred already,
            # determines the number of times a subarray with sum k
            # has occurred up to the current index
            count += mp.get(cum_sum - k, 0)
            # add the current sum
            mp[cum_sum] += 1

        return count