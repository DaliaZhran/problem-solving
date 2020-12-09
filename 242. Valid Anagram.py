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
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


# Approach #2 (Hash map) [Accepted]
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


# Approach #3 (2 Hash maps) [Accepted]
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)


# hash table
# if unicode letters are included, then this approach won't work
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        char_frequencies = [0] * 26
        for i in range(len(s)):
            char_frequencies[ord(s[i]) - ord("a")] += 1
            char_frequencies[ord(t[i]) - ord("a")] -= 1

        for ch in char_frequencies:
            if ch != 0:
                return False
        return True
