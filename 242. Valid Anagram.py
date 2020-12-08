# https://leetcode.com/problems/valid-anagram/

"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true


Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

# Approach #1 (Sorting) [Accepted]


# Approach #2 (Hash Table) [Accepted]
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_chars = Counter(s)
        for l in t:
            if s_chars[l]:
                s_chars[l] -= 1
            else:
                return False
        return True
