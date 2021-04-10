# https://leetcode.com/problems/happy-number/

"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

# Approach 1: Detect Cycles with a HashSet

# idea is based on detecting a cycle
# Time: O(logn)
# Space: O(1)
class Solution:
    def isHappy(self, n: int) -> bool:
        def calc_digits(num):
            res = 0
            while num > 0:
                res += (num % 10) ** 2
                num //= 10
            return res

        curr_num = n
        fast_num = calc_digits(n)
        while fast_num != 1 and curr_num != fast_num:
            curr_num = calc_digits(curr_num)
            fast_num = calc_digits(calc_digits(fast_num))
        return fast_num == 1
