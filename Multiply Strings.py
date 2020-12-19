# https://leetcode.com/problems/multiply-strings/

"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
"""

# Time -> O(nm)
# Space -> O(n+m)
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0] * (len(num1) + len(num2))
        pos = len(result) - 1

        for i in range(len(num1) - 1, -1, -1):
            temp_pos = pos
            for j in range(len(num2) - 1, -1, -1):
                product = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                result[temp_pos] += product
                result[temp_pos - 1] += result[temp_pos] / 10
                result[temp_pos] %= 10
                temp_pos -= 1
            pos -= 1

        pt = 0
        while pt < len(result) - 1 and result[pt] == 0:
            pt += 1

        return "".join(map(str, result[pt:]))
