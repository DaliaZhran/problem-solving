# https://leetcode.com/problems/sqrtx/
"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.


Example 1:

Input: x = 4
Output: 2
"""

# Brute Force -> start from 1 till we reach n or a num > n
# Approach 1: Pocket Calculator Algorithm -> use log for x^1/2

# Binary Search
# Time: O(log N)
# Space: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            mid = left + (right - left) // 2
            target = mid * mid
            if target > x:
                right = mid - 1
            elif target < x:
                left = mid + 1
            else:
                return mid

        return right  # at the end positions will be --> right, left --> left would be the answer since we truncate the decimal digits


# Newton's method
# Bit Manipulation
