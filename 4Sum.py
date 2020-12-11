# https://leetcode.com/problems/4sum/

"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.kSum(nums, target, 4)

    def kSum(self, nums, target, k):
        res = []
        if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
            return res
        if k == 2:
            return self.twoSum(nums, target)
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for _, set in enumerate(self.kSum(nums[i + 1 :], target - nums[i], k - 1)):
                    res.append([nums[i]] + set)
        return res

    def twoSum(self, nums, target):
        res = []
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            sum = nums[lo] + nums[hi]
            if sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                lo += 1
            elif sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1
        return res