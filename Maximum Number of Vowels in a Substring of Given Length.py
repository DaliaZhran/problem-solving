# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""
Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
"""

# Sliding Window
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        max_count = 0
        curr_count = 0
        start = 0
        for end in range(len(s)):
            if s[end] in vowels:
                curr_count += 1

            if end - start + 1 > k:  # we can replace start with end - k (since the window size is fixed)
                if s[start] in vowels:
                    curr_count -= 1
                start += 1

            max_count = max(max_count, curr_count)
        return max_count
