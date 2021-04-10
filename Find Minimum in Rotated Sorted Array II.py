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

# Approach 1: Linear search

# Approach 2: Binary Search
# Time: O(log N)
# Space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            pivot = l + (r - l) // 2
            # we compare with right element because mid cannot == right
            if nums[pivot] > nums[r]:  # left is sorted
                l = pivot + 1
            elif nums[pivot] < nums[r]:  # right is sorted
                r = pivot
            else:  # right part are all duplicates of nums[mid]
                r -= 1

        return nums[l]


# Examples
# [3,1,3]
# [1,1,1,2,3] -> infinite loop -> memory overflow if we did not use the last condition
# [1,2,3,3,3] -> if we moved the left index instead of right, we would miss the minimum since we are comparing with right index


# maybe we can check possibility of doing it from left -> it wont work in some cases like [1,2,3,3,3]
