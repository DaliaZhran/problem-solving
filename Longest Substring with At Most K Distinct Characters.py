# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
"""
from collections import defaultdict


# * Sliding Window
# Time -> O(N)
# Space -> O(1)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        start = 0
        length = 0
        char_map = defaultdict(int)
        for end in range(len(s)):
            char_map[s[end]] += 1

            while len(char_map) > k:
                char_map[s[start]] -= 1
                if char_map[s[start]] == 0:
                    del char_map[s[start]]
                start += 1

            length = max(length, end - start + 1)

        return length
