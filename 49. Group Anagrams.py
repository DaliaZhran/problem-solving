# https://leetcode.com/problems/group-anagrams/

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

# time -> O(N * KlogK)
# space -> O(KN)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        groups = defaultdict(list)
        for s in strs:
            groups["".join(sorted(s))].append(s)  # sorting is space O(K)

        return groups.values()


# time -> O(KN)
# space -> O(KN)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for l in s:
                count[ord(l) - ord("a")] += 1

            groups[tuple(count)].append(s)

        return groups.values()


# One more approach can be using Trie Tree. We build the trie tree iterating through the list once with sorted(str) and at the leaf node (End of word), we store the index of the original list. However, same complexity as first approach with code complication

# use primes to caculate hash key