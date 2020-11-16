# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:
Input: [2,2,2,0,1]
Output: 0

Example 2:
Input: [3,3,1,3]
Output: 1
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            pivot = l + (r - l) // 2
            if nums[pivot] > nums[r]:
                l = pivot + 1
            elif nums[pivot] < nums[r]:
                r = pivot
            else:  # when num[mid] and num[hi] are same
                r -= 1

        return nums[l]


# maybe we can check possibility of doing it from left
