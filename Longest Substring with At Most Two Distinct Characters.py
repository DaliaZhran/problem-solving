# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
"""

# * Sliding Window
# Time -> O(N)
# Space -> O(1)
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        chars_freq = defaultdict(int)
        longest_str = 0
        start = 0

        for end in range(n):
            right = s[end]
            chars_freq[right] += 1

            while len(chars_freq) > 2:
                left = s[start]
                start += 1
                chars_freq[left] -= 1
                if chars_freq[left] == 0:
                    del chars_freq[left]

            longest_str = max(longest_str, end - start + 1)

        return longest_str