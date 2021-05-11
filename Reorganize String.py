# https://leetcode.com/problems/reorganize-string/

"""
Given a string s, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
Note:

s will consist of lowercase letters and have length in range [1, 500].
"""
from collections import Counter
from heapq import heappop, heappush


# general solution for any k
# Time: O(n log n) -> we will pass by each character in the array once and logn for inserting into heaps
# space: O(n)
class Solution:
    def reorganizeString(self, S: str) -> str:
        cnt = Counter(S)
        heap = []
        for ch, ch_count in cnt.items():
            heappush(heap, (-ch_count, ch))

        res = []
        next_heap = []
        k = 2
        while heap:
            if not res or res[-1] != heap[0][1]:
                ch_count, ch = heappop(heap)
                res.append(ch)
                if ch_count + 1 != 0:
                    heappush(next_heap, (ch_count + 1, ch))
                k -= 1
            else:
                return ""

            if k == 0:
                k = 2
                while next_heap:
                    heappush(heap, heappop(next_heap))

            if not heap:
                heap = next_heap
                next_heap = []

        return "".join(res)


# specific solution for k = 2
# Time: O(n log n)
# space: O(n)
class Solution:
    def reorganizeString(self, S: str) -> str:
        freq_map = {}
        for char in S:
            freq_map[char] = freq_map.get(char, 0) + 1

        max_heap = []
        for char, freq in freq_map.items():
            heappush(max_heap, (-freq, char))

        prev_char, prev_freq = None, 0
        result = []
        while max_heap:
            freq, char = heappop(max_heap)
            if prev_char and -prev_freq > 0:
                heappush(max_heap, (prev_freq, prev_char))
            result.append(char)
            prev_char, prev_freq = char, freq + 1

        return "".join(result) if len(result) == len(S) else ""
