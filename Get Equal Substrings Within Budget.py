# https://leetcode.com/problems/get-equal-substrings-within-budget/

"""
You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.

You are also given an integer maxCost.

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of twith a cost less than or equal to maxCost.

If there is no substring from s that can be changed to its corresponding substring from t, return 0.

Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.
"""

# Sliding Window
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_len = 0
        start = 0
        for end in range(len(s)):
            maxCost -= abs(ord(s[end]) - ord(t[end]))
            if maxCost < 0:
                maxCost += abs(ord(s[start]) - ord(t[start]))
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len


# check prefix sum
# https://leetcode.com/problems/get-equal-substrings-within-budget/discuss/393419/Simply-Simple-Python-Solution-with-explanation-Prefix-sum
