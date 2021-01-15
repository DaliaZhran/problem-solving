# https://leetcode.com/problems/reverse-string-ii/

"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""

# Intuition
# Time : O(N)
# Space : O(N)
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        arr = list(s)
        for i in xrange(0, len(s), 2 * k):
            arr[i : i + k] = arr[i + k : i - 1 : -1]
        return "".join(arr)


# Recursion
# Time : O(N)
# Space : O(N)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]
        if len(s) < 2 * k:
            return s[:k][::-1] + s[k:]

        return s[:k][::-1] + s[k : 2 * k] + self.reverseStr(s[2 * k :], k)
