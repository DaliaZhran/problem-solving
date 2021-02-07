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
        def find_first_position(start, end):
            while start < end:
                mid = start + (end - start) // 2
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid
            return start

        def find_last_position(start, end):
            while start < end:
                mid = (start + end + 1) // 2
                if nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid
            return start

        n = len(nums)
        left = find_first_position(0, n - 1)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = find_last_position(left, n - 1)
        return [left, right]


# Binary Search - 2 passes - better implementation
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(start, end, isLeft):
            while start < end:
                mid = start + (end - start) // 2
                if nums[mid] > target or (isLeft and nums[mid] == target):
                    end = mid
                else:
                    start = mid + 1

            return start

        n = len(nums)
        left = binary_search(0, n - 1, True)  # find first position
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = binary_search(left, n - 1, False) - 1  # find last position -> find smallest number greater than the target and then decrement its index
        return [left, right]


# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14699/Clean-iterative-solution-with-two-binary-searches-(with-explanation)

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14701/A-very-simple-Java-solution-with-only-one-binary-search-algorithm