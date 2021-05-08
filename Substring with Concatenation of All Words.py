# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

"""
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
"""

from collections import Counter, defaultdict
from typing import List


# Sliding Window
# Time: O(len(s) * len(words))
# Space: O(n) -> n = len(words)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        mp = Counter(words)
        wcount = len(words)
        wsize = len(words[0])

        for start in range(len(s) - wsize * wcount + 1):
            seen = defaultdict(int)
            for w_idx in range(wcount):
                wstart = start + w_idx * wsize
                word = s[wstart : wstart + wsize]

                seen[word] += 1
                if seen[word] > mp[word]:  # if word does not exist in counter mp, it returns 0
                    break

                if w_idx + 1 == wcount:
                    res.append(start)
        return res


# more readable solution
class Solution(object):
    def findSubstring(self, s, words):
        if len(words) == 0 or len(words[0]) == 0:
            return []

        wordLen = len(words[0])
        wordsCount = len(words)
        wordFreq = {}
        indecies = []

        for word in words:
            if word not in wordFreq:
                wordFreq[word] = 0
            wordFreq[word] += 1

        for i in range(len(s) - wordLen * wordsCount + 1):
            wordsSeen = {}
            for j in range(0, wordsCount):
                start = i + j * wordLen
                word = s[start : start + wordLen]

                if word not in wordFreq:
                    break

                if word not in wordsSeen:
                    wordsSeen[word] = 0
                wordsSeen[word] += 1

                if wordsSeen[word] > wordFreq[word]:
                    break

                if j + 1 == wordsCount:
                    indecies.append(i)
        return indecies
