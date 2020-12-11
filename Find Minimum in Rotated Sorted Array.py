# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums, return the minimum element of this array.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[r] >= nums[0]:
            return nums[0]

        while l <= r:
            pivot = l + (r - l) // 2
            if nums[pivot] > nums[pivot + 1]:
                return nums[pivot + 1]
            elif nums[pivot] < nums[pivot - 1]:
                return nums[pivot]
            else:
                if nums[pivot] > nums[0]:
                    l = pivot + 1
                else:
                    r = pivot - 1


# good explaination
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/158940/Beat-100%3A-Very-Simple-(Python)-Very-Detailed-Explanation
# shorter implementation
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/48484/A-concise-solution-with-proof-in-the-comment