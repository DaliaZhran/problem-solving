# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
"""
from collections import defaultdict


# * Sliding Window
# Time -> O(N)
# Space -> O(1)
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        start = 0
        length = 0
        char_map = defaultdict(int)
        for end in range(len(s)):
            char_map[s[end]] += 1

            while len(char_map) > 2:
                char_map[s[start]] -= 1
                if char_map[s[start]] == 0:
                    del char_map[s[start]]
                start += 1

            length = max(length, end - start + 1)

        return length
