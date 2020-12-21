# https://leetcode.com/problems/valid-palindrome-ii/

"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
"""

# Approach #1: Brute Force [Time Limit Exceeded]
# time -> O(N^2)
# space -> O(N)
class Solution(object):
    def validPalindrome(self, s):
        for i in xrange(len(s)):
            t = s[:i] + s[i + 1 :]
            if t == t[::-1]:
                return True

        return s == s[::-1]


# time -> O(n)
# space -> O(n)
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                option1 = s[:l] + s[l + 1 :]
                option2 = s[:r] + s[r + 1 :]
                return option1 == option1[::-1] or option2 == option2[::-1]

            l += 1
            r -= 1

        return True


# time -> O(n)
# space -> O(1)
class Solution(object):
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)

            l += 1
            r -= 1

        return True
