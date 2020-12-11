# https://leetcode.com/problems/sort-characters-by-frequency/

"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
"""

from collections import Counter

# * heap and hashmap
# time -> O(n) + O(nlogn) -> O(nlogn)
# space -> O(n) for output
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        max_heap = []
        for ch, freq in count.items():
            heappush(max_heap, (-freq, ch))

        s = []
        while max_heap:
            freq, ch = heappop(max_heap)
            s.append(ch * -freq)

        return "".join(s)


# * another implementation
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        s = []
        for ch, freq in count.most_common():
            s.append(ch * freq)
        return "".join(s)


# * good O(n) solution using 2 hashmaps

# Frequency of a character can vary from 0 to len(s).
# Create a hashmap H1 of character to character frequency for the input string.
# Iterate H1 to create hashmap H2 with key as frequency and value as substrings of repeated strings with length as the frequency.
# Finally lookup all potential frequencies in decreasing order in H2 and produce the final result.
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c1, c2 = Counter(s), {}
        for k, v in c1.items():
            c2.setdefault(v, []).append(k * v)
        return "".join(["".join(c2[i]) for i in range(len(s), -1, -1) if i in c2])