# https://leetcode.com/problems/top-k-frequent-words/

"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
"""

from collections import Counter, defaultdict
from heapq import heappop, heappush
from typing import List


# Sort
# time : O(nlogn)
# space: O(n)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordsDict = Counter(words)
        res = sorted(wordsDict, key=lambda x: (-wordsDict[x], x))
        return res[:k]


# time : O(nlogn)
# space: O(n)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequencies = Counter(words)
        heap = []

        for w, freq in frequencies.items():
            heappush(heap, (-freq, w))

        res = []
        while heap and k:
            freq, w = heappop(heap)
            res.append(w)
            k -= 1

        return res


# just for reference
# https://leetcode.com/problems/top-k-frequent-words/discuss/431008/Summary-of-all-the-methods-you-can-imagine-of-this-problem
