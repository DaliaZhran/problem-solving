# https://leetcode.com/problems/single-number-iii/

"""
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

Follow up: Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""
from collections import Counter


# * Hashmap
# time: O(n)
# space: O(n)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        freq_map = Counter(nums)
        # freq_map = defaultdict(int)
        # for num in nums:
        #     freq_map[num] += 1
        for num, freq in freq_map.items():
            if freq == 1:
                ans.append(num)
        return ans


# time: O(n)
# space: O(1)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # all nums appear twice except two so the xoring will make them 0 and the xor of the 2 odd-occuring numbers
        bitmask = 0
        for num in nums:
            bitmask ^= num

        # get the first different 1
        # since we have 2 numbers remaining in the bitmask, their ones are xored and 0 and their different bits are the ones in the bitmask
        diff = bitmask & (-bitmask)  # isolate the first one

        x = 0
        for num in nums:
            if num & diff:  # get only one odd-occuring number
                x ^= num

        # x ^ y = bitmask
        # bitmask ^ x = y
        # bitmask ^ y = x
        return [x, bitmask ^ x]
