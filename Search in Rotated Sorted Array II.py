# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.
"""

# the trick here is when the all elements in the first half is equal to the mid
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        if right == -1:
            return False

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            # moving left or right does not make a difference given we compare with element on its side
            # if nums[mid] == nums[right]:
            #     right -= 1
            if nums[mid] == nums[left]:
                left += 1
            elif nums[mid] > nums[right]:  # left is sorted
                if target < nums[mid] and target >= nums[left]:  # target in left part of mid
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # right is sorted
                if target > nums[mid] and target <= nums[right]:  # target in right part of mid
                    left = mid + 1
                else:
                    right = mid - 1

        return False
