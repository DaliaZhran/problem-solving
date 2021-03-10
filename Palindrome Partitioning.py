# https://leetcode.com/problems/palindrome-partitioning/

"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
"""

# Backtracking
# Time: O(n * 2^n) where n is the length of s
# Space: O(n)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def tryParititon(s, curr_list):
            if s == "":
                result.append(curr_list[:])
                return

            for hi in range(1, len(s) + 1):
                left = s[:hi]
                right = s[hi:]
                if self.isPalindrome(left):
                    curr_list.append(left)
                    tryParititon(right, curr_list)
                    curr_list.pop()

        result = []
        tryParititon(s, [])
        return result

    def isPalindrome(self, s):
        lo = 0
        hi = len(s) - 1
        while lo <= hi and s[lo] == s[hi]:
            lo += 1
            hi -= 1
        return lo >= hi


# Backtracking -> using pointers
# Time: O(n * 2^n) where n is the length of s
# Space: O(n)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def tryParititon(s, curr_list, lo):
            if lo == n:
                result.append(curr_list[:])
                return

            for hi in range(lo, n):
                if self.isPalindrome(s, lo, hi):
                    curr_list.append(s[lo : hi + 1])
                    tryParititon(s, curr_list, hi + 1)
                    curr_list.pop()

        n = len(s)
        result = []
        tryParititon(s, [], 0)
        return result

    def isPalindrome(self, s, lo, hi):
        while lo <= hi and s[lo] == s[hi]:
            lo += 1
            hi -= 1
        return lo >= hi
