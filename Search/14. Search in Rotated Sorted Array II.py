# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.
"""

# the trick here is when the all elements in the first half is equal to the mid
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 0:
            return False
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[l]:
                l += 1
                # continue
            elif nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False