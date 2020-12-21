# https://leetcode.com/problems/3sum-smaller/

"""
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Follow up: Could you solve it in O(n2) runtime?
"""

# * Note: we may need to check if there are duplicates or not

# * Approach 1: Brute Force -> O(n^3)

# * Approach 2: Binary Search -> O(n^2 logn)
# time ->  O(n^2 logn)
# space -> O(n)
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
            for j in range(i + 1, len(nums) - 1):
                max_right_index = self.binarySearch(nums, j, target - nums[i] - nums[j])
                count += max_right_index - j
        return count

    def binarySearch(self, nums, start, target):
        left, right = start, len(nums) - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid - 1
        return left


# * Approach 3: 2 pointers approach
# time -> O(nlogn) + O(n^2)
# space -> O(n) for sorting
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
