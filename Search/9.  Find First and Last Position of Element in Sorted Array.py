# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?
"""

# * Intuitive - O(n)
class Solution:
    def searchRange(self, nums, target):
        # find the index of the leftmost appearance of `target`. if it does not
        # appear, return [-1, -1] early.
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        # find the index of the rightmost appearance of `target` (by reverse
        # iteration). it is guaranteed to appear.
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]


# * Binary Search - 2 passes
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if not nums:
            return res
        n = len(nums)
        l, r = 0, n - 1
        # find start of range
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] == target:
            res[0] = l
        else:
            return res

        # find end of range
        r = n - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid

        res[-1] = r
        return res


# Binary Search - 2 passes - better implementation
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(isLeft):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] > target or (isLeft and target == nums[mid]):
                    right = mid
                else:
                    left = mid + 1
            return left

        if not nums:
            return [-1, -1]
        left = binarySearch(True)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, binarySearch(False) - 1]


# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14699/Clean-iterative-solution-with-two-binary-searches-(with-explanation)