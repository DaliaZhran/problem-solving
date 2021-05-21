# https://leetcode.com/problems/repeated-dna-sequences/
"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.


Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
"""
from typing import List


# sliding window -> fixed window
# time -> O(N - L) where N is len(s) and L is len(DNA sequence)
# space -> O(N - L)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = 10
        seqs = set()
        res = set()

        for i in range(len(s) - n + 1):
            if s[i : i + n] in seqs:
                res.add(s[i : i + n])
            else:
                seqs.add(s[i : i + n])

        return res
