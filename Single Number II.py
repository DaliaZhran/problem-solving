# https://leetcode.com/problems/single-number-ii/

"""
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
"""
# * Set
# time: O(n)
# space: O(n)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (3 * sum(set(nums)) - sum(nums)) // 2


# * Hashmap
# time: O(n)
# space: O(n)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we can replace the first for loop with a counter
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        for num, freq in freq_map.items():
            if freq == 1:
                return num


# * Bit Manipulation
# good explaination -> https://lenchen.medium.com/leetcode-137-single-number-ii-31af98b0f462
# time: O(n)
# space: O(1)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen_once, seen_twice = 0, 0
        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once
