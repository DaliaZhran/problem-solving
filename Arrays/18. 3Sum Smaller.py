# https://leetcode.com/problems/3sum-smaller/

"""
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Follow up: Could you solve it in O(n2) runtime?
"""

# * Note: we may need to check if there are duplicates or not

# intuitive sol -> O(n^3)

# 2 pointers approach
# time -> O(nlogn) + O(n^2)
# space -> O(logn) to O(n) depending on the sorting algorithm
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count = 0
        for i in xrange(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] >= target:
                    right -= 1
                else:
                    count += right - left
                    left += 1

        return count
