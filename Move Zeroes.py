# https://leetcode.com/problems/move-zeroes/

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        res = []
        for i in range(len(nums)):
            if nums[i] != 0:
                res.append(nums[i])

        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(0)

        for i in range(len(nums)):
            nums[i] = res[i]


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: N'
        one Do not return anything, modify nums in-place instead.
        """
        res = []
        zeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                res.append(nums[i])
            else:
                zeros += 1
        for i in range(zeros):
            res.append(0)

        for i in range(len(nums)):
            nums[i] = res[i]


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_num_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_num_pos] = nums[i]
                last_num_pos += 1

        for i in range(last_num_pos, len(nums)):
            nums[i] = 0


# most optimal operations
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_num_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_num_pos], nums[i] = nums[i], nums[last_num_pos]
                last_num_pos += 1
