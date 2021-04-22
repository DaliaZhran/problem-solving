# https://leetcode.com/problems/permutation-in-string/

"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_frequency = Counter(s1)
        start, matched = 0, 0

        for end in range(len(s2)):
            right = s2[end]
            if right in char_frequency:
                char_frequency[right] -= 1
                if char_frequency[right] == 0:
                    matched += 1

            if matched == len(char_frequency):
                return True

            if end >= len(s1) - 1:
                left = s2[start]
                start += 1
                if left in char_frequency:
                    if char_frequency[left] == 0:
                        matched -= 1
                    char_frequency[left] += 1
        return False
