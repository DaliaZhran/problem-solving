# https://leetcode.com/problems/contains-duplicate-ii/

"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
"""

# Time Limit Exceeded
# Time -> O(n^2)
# Space -> O(1)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, min(i + k + 1, n)):
                if abs(j - i) <= k and nums[i] == nums[j]:
                    return True
        return False


# instead of looping through the window of size k again, we can use a hashset to keep track of the numbers in the current window
# Time -> O(n)
# Space -> O(min(n,k))
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False
