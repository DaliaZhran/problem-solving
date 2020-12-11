# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

"""
Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index, otherwise return -1. However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.

"""
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

# * just determine the boundaries first, then normal BS
class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0

        r = 1
        while reader.get(r) < target:
            r *= 2
        l = r // 2

        while l <= r:
            mid = l + (r - l) // 2
            num = reader.get(mid)
            if num == target:
                return mid
            elif num > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1  # not found
