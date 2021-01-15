# https://leetcode.com/problems/next-permutation/

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]
"""

# Lexicographical Order
# [1,2,3]
# [1,3,2]
# [2,1,3]
# [2,3,1]
# [3,1,2]
# [3,2,1]


# * Approach 1: Brute Force
# Time -> O(n!)
# Space -> O(n) Since an array will be used to store the permutations


# * Approach 2: Single Pass Approach
# Time -> O(n)
# Space -> O(1)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the longest non increasing suffix and identify pivot
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        # find rightmost successor to pivot in the suffix
        if i >= 0:
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # swap the pivot
            nums[j], nums[i] = nums[i], nums[j]

        # reverse the suffix
        self.reverseList(nums, i + 1)

    def reverseList(self, nums, start):
        i = start
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return nums


# Photo -> https://leetcode.com/problems/next-permutation/discuss/13994/Readable-code-without-confusing-ij-and-with-explanation