# https://leetcode.com/problems/plus-one/

"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""

# Time complexity : O(N) since it's not more than one pass along the input list.
# Space complexity : O(1) when digits contains at least one not-nine digit, and O(N) otherwise.
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        i = n - 1
        carry = 1
        while i >= 0:
            num = digits[i] + carry
            carry = num // 10
            digits[i] = num % 10
            if carry == 0:
                return digits
            i -= 1

        return [1] + digits
