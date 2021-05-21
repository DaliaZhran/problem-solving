# https://leetcode.com/problems/find-all-anagrams-in-a-string/

"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""
from collections import Counter
from typing import List


# sliding window
# time -> O(n) where n is len(s)
# space -> O(1) since both s and p consist of english letters O(26)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        len_s = len(s)
        len_p = len(p)
        if len_s < len(p):
            return res

        p_char_freq = Counter(p)
        s_char_freq = Counter()

        for i in range(len_s):
            s_char_freq[s[i]] += 1

            if i >= len_p:
                if s_char_freq[s[i - len_p]] == 1:
                    del s_char_freq[s[i - len_p]]
                else:
                    s_char_freq[s[i - len_p]] -= 1

            if s_char_freq == p_char_freq:
                res.append(i - len_p + 1)

        return res


# sliding window
# time -> O(n) where n is len(s)
# space -> O(1) since both s and p consist of english letters O(26)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        len_p = len(p)
        len_s = len(s)
        if len_s < len_p:
            return []

        s_chars = [0] * 26
        p_chars = [0] * 26
        for i in p:
            p_chars[ord(i) - ord("a")] += 1

        for i in range(len_s):
            s_chars[ord(s[i]) - ord("a")] += 1
            if i >= len_p:
                s_chars[ord(s[i - len_p]) - ord("a")] -= 1

            if s_chars == p_chars:
                res.append(i - len_p + 1)

        return res


# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.
