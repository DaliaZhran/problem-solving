# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
"""

# * Sliding Window
# Time -> O(N)
# Space -> O(1)
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        chars_freq = defaultdict(int)
        longest_str = 0
        start = 0

        for end in range(n):
            right = s[end]
            chars_freq[right] += 1

            while len(chars_freq) > k:
                left = s[start]
                start += 1
                chars_freq[left] -= 1
                if chars_freq[left] == 0:
                    del chars_freq[left]

            longest_str = max(longest_str, end - start + 1)

        return longest_str