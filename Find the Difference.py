# https://leetcode.com/problems/find-the-difference/
'''
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

 

Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
'''

from collections import defaultdict


# 1
class Solution(object):
    """
    dictionary
    """
    def findTheDifference(self, s, t):
        dic = defaultdict(int)
        for ch in s:
            dic[ch] += 1
        for ch in t:
            if ch not in dic:
                return ch
            else:
                dic[ch] -= 1

# 2
class Solution(object):
    """
    difference
    """
    def findTheDifference(self, s, t):
        diff = 0
        for i in range(len(s)):
            diff -= ord(s[i])
            diff += ord(t[i])
        diff += ord(t[-1])
        return chr(diff)

# 3 
class Solution(object):
    """
    xor
    """
    def findTheDifference(self, s, t):
        code = 0
        for ch in s + t:
            code ^= ord(ch)
        return chr(code)

# 3 enhanced -> no concat
class Solution(object):
    """
    xor
    """
    def findTheDifference(self, s, t):
        code = 0
        for ch in s:
            code ^= ord(ch)
        for ch in t:
            code ^= ord(ch)
        return chr(code)
