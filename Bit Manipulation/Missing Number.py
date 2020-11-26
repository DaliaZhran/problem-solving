# https://leetcode.com/problems/missing-number/

"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""


# Sol 1 -> utilizing the idea of series 1,2,3,4,5,n = n(n+1)/2
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        mx = len(nums)
        # sum(nums) instead
        for n in nums:
            s += n

        v = mx * (mx + 1) / 2

        return v - s if s != v else 0


# Sol 2 -> xor indecies & array nums -> use enumerate instead of range
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s1 = n
        for i in range(n):
            s1 ^= i ^ nums[i]
        return s1


# Sol 3 -> difference of 2 sets
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        return ((set(list(range(n + 1))) - (set(nums)))).pop()
