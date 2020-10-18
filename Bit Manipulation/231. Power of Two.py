# time -> O(1)
# Space -> O(1)
# ...
# Given an integer, write a function to determine if it is a power of two.


import math


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
        return not (n & (n - 1))

