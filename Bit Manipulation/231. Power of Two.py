# https://leetcode.com/problems/power-of-two

"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
"""

# time -> O(log2 n)
# Space -> O(1)
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1


# time -> O(1)
# Space -> O(1)
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #         if n < 0:
        #             return False
        #         count = 0
        #         while n:
        #             count += 1 & n
        #             n = n >> 1

        #         return count == 1

        if n < 0:
            return False
        return not (n & (n - 1))  # turn off the first 1 (which should be the only one)


# Depending on the fact that a number of power 2 has only one 1-bit
# time -> O(1)
# Space -> O(1)
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        return n & -n == n