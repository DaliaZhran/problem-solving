# https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

# * Approach 1: Brute Force
# Time complexity : O(n^3)
# Space complexity : O(min(m,n)). We need O(k) space for the sliding window, where k is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the charset/alphabet m.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):  # n+1 for cases of string of len 1 to enter second loop
                # if self.isStringUnique(s[i:j]): # instead of passing a copy of the string, just pass the indecies
                if self.isStringUnique(s, i, j):
                    res = max(res, j - i)
                else:
                    break
        return res

    def isStringUnique(self, string, start_index, end_index):
        chars_set = set()
        for i in range(start_index, end_index):
            if string[i] in chars_set:
                return False
            else:
                chars_set.add(string[i])
        return True


# * Straightforward Sliding Window
# Time complexity : O(2n) = O(n). In the worst case each character will be visited twice by i and j.
# Space complexity : O(min(m,n)). Same as Brute Force.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        chars_set = set()
        count = 0
        while l <= r and r < len(s):  # l<=r to consider for cases of 1 length
            if s[r] not in chars_set:
                set.add(s[r])
                count = max(count, r - l + 1)
                r += 1
            else:
                chars_set.remove(s[l])
                l += 1

        return count


# * Optimized Sliding Window
# Time complexity : O(n). Index j will iterate n times.
# Space complexity (HashMap) : O(min(m,n)). Same as the previous approach.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, end = 0, 0
        chars_index_map = {}
        count = 0
        while start <= end and end < len(s):
            if s[end] in chars_index_map:
                l = max(chars_index_map[s[end]], start)  # we start from the next element right to the first occurance of the duplicate

            count = max(count, end - l + 1)
            chars_index_map[s[end]] = end + 1
            end += 1
        return count


"""
If we know that the charset is rather small, we can replace the Map with an integer array as direct access table.

Commonly used tables are:

int[26] for Letters 'a' - 'z' or 'A' - 'Z'
int[128] for ASCII
int[256] for Extended ASCII
"""
