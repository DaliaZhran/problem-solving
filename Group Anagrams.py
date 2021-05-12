# https://leetcode.com/problems/group-anagrams/

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
from collections import defaultdict
from typing import List


# time -> O(N * KlogK)
# space -> O(KN)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for w in strs:
            groups["".join(sorted(w))].append(w)

        return groups.values()


# using the fact that words consists only of lower english letters
# time -> O(KN)
# space -> O(KN)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for w in strs:
            count = [0] * 26
            for ch in w:
                count[ord(ch) - ord("a")] += 1
            groups[tuple(count)].append(w)

        return groups.values()


# use unique prime multiplication to caculate hash key
# time -> O(KN)
# space -> O(N)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        primes = {
            "a": 2,
            "b": 3,
            "c": 5,
            "d": 7,
            "e": 11,
            "f": 13,
            "g": 17,
            "h": 19,
            "i": 23,
            "j": 29,
            "k": 31,
            "l": 37,
            "m": 41,
            "n": 43,
            "o": 47,
            "p": 53,
            "q": 59,
            "r": 61,
            "s": 67,
            "t": 71,
            "u": 73,
            "v": 79,
            "w": 83,
            "x": 89,
            "y": 97,
            "z": 101,
        }

        groups = defaultdict(list)
        for w in strs:
            product = 1
            for ch in w:
                product *= primes[ch]

            groups[product].append(w)
        return groups.values()


# One more approach can be using Trie Tree. We build the trie tree iterating through the list once with sorted(str) and at the leaf node (End of word), we store the index of the original list. However, same complexity as first approach with code complication
