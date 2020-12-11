# https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

# Approach 1: Brute Force


# Straightforward Sliding Window
# Time complexity : O(2n) = O(n). In the worst case each character will be visited twice by i and j.

# Space complexity : O(min(m,n)). Same as the previous approach. We need O(k) space for the sliding window, where k is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the charset/alphabet m.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        freq_map = {}
        count = 0
        while l <= r and r < len(s):
            if s[r] not in freq_map:
                freq_map[s[r]] = 1
                count = max(count, r - l + 1)
                r += 1
            else:
                del freq_map[s[l]]
                l += 1

        return count


# Optimized Sliding Window
# Time complexity : O(n). Index j will iterate nn times.

# Space complexity (HashMap) : O(min(m,n)). Same as the previous approach.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        chars_index_map = {}
        count = 0
        while l <= r and r < len(s):
            if s[r] in chars_index_map:
                l = max(chars_index_map[s[r]], l)

            count = max(count, r - l + 1)
            chars_index_map[s[r]] = r + 1
            r += 1
        return count
