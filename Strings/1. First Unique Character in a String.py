# https://leetcode.com/problems/first-unique-character-in-a-string/

"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
"""

# * map to keep track of the duplicates
# time -> O(2n)
# space -> O(1) since alphabet is just 26 letters
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars_freq = {}
        for ch in s:
            chars_freq[ch] = chars_freq.get(ch, 0) + 1

        for i, ch in enumerate(s):
            if chars_freq[ch] == 1:
                return i
        return -1