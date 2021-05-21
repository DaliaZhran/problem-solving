# https://leetcode.com/problems/permutation-in-string/

"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
"""
from collections import Counter


# sliding window
# time -> O(n) where n is len(s2)
# space -> O(1)
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


# sliding window -> fixed window
# time -> O(n) where n is len(s2)
# space -> O(1) since both s1 and s2 consist of english letters O(26)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ns1 = len(s1)
        s1_count = Counter(s1)
        s2_count = Counter()

        for i, ch in enumerate(s2):
            s2_count[ch] += 1

            if i >= ns1:
                if s2_count[s2[i - ns1]] == 1:
                    del s2_count[s2[i - ns1]]
                else:
                    s2_count[s2[i - ns1]] -= 1

            if s1_count == s2_count:
                return True

        return False


# sliding window -> fixed window
# time -> O(n) where n is len(s2)
# space -> O(1) since both s1 and s2 consist of english letters O(26)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ns1 = len(s1)
        s1_count = [0] * 26
        s2_count = [0] * 26

        for ch in s1:
            s1_count[ord(ch) - ord("a")] += 1

        for i, ch in enumerate(s2):
            s2_count[ord(ch) - ord("a")] += 1

            if i >= ns1:
                s2_count[ord(s2[i - ns1]) - ord("a")] -= 1

            if s1_count == s2_count:
                return True

        return False
