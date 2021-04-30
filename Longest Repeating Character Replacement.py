# https://leetcode.com/problems/longest-repeating-character-replacement/

"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations. 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
"""


# Approach 1: Brute Force -> O(n^2)

# Approach 2: DP -> Not good option

from collections import defaultdict


# Approach 3: Sliding Window -> O(n)
# Space: O(1) since its only upper case english letters
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        max_char_count = 0
        max_length = 0
        char_map = defaultdict(int)
        for end, end_ch in enumerate(s):
            char_map[end_ch] += 1
            max_char_count = max(max_char_count, char_map[end_ch])
            while end - start + 1 - max_char_count > k:
                char_map[s[start]] -= 1
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length
