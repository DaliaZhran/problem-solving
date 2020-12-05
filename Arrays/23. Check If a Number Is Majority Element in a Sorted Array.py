# https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

"""
Given an array nums sorted in non-decreasing order, and a number target, return True if and only if target is a majority element.

A majority element is an element that appears more than N/2 times in an array of length N.

 

Example 1:

Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
Output: true
Explanation: 
The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 > 9/2 is true.
"""

# * Brute Force
# time -> O(n)
# space -> O(1)
class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        count = 0
        for num in nums:
            if num == target:
                count += 1
            if count != 0 and num != target:
                break
        return len(nums) // 2 < count


# Binary Search
# time -> O(logn)
# space -> O(1)
# get first index of target and first index of smallest num greater than target, then subtract
def isMajorityElement(self, nums, target):
    def search(a, x):
        lo, hi = 0, len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    N = len(nums)
    if nums[N // 2] != target:
        return False
    lo = search(nums, target)
    hi = search(nums, target + 1)
    return hi - lo > N // 2
