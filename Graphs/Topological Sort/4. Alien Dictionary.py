# https://leetcode.com/problems/alien-dictionary/
"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
"""
from collections import defaultdict


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        G = defaultdict(set)
        indegree = defaultdict(int)
        for word in words:
            for l in word:
                indegree[l] = 0

        for first_word, second_word in zip(words, words[1:]):  # gives us every 2 adj items
            for c, d in zip(first_word, second_word):  # compares each letter of the words
                if c != d:
                    if d not in G[c]:
                        G[c].add(d)
                        indegree[d] += 1
                    break
            else:
                if len(second_word) < len(first_word):
                    return ""

        nonDependent = deque()
        for node in indegree:
            if indegree[node] == 0:
                nonDependent.append(node)

        res = []
        while nonDependent:
            node = nonDependent.pop()
            res.append(node)
            for adjNode in G[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    nonDependent.append(adjNode)
        if len(res) < len(indegree):
            return ""
        return "".join(res)
