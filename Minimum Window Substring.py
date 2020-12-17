# https://leetcode.com/problems/minimum-window-substring/

"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""

        len_s = len(s)
        t_chars_freq = Counter(t)
        required = len(t_chars_freq)
        min_length = len_s + 1
        matched = 0
        start, substr_start = 0, 0

        for end in range(len_s):
            right = s[end]
            if right in t_chars_freq:
                t_chars_freq[right] -= 1  # decrement because we started with chars frequency in t
                if t_chars_freq[right] == 0:
                    matched += 1

            while matched == required:  # shrink the window
                if min_length > end - start + 1:
                    min_length = end - start + 1
                    substr_start = start

                left = s[start]
                start += 1
                if left in t_chars_freq:
                    if t_chars_freq[left] == 0:
                        matched -= 1
                    t_chars_freq[left] += 1

        if min_length > len_s:
            return ""
        return s[substr_start : substr_start + min_length]
