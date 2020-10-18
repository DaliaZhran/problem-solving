# https://leetcode.com/problems/sequence-reconstruction/

"""
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.
"""

from collections import deque


class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        # values = {x for seq in seqs for x in seq}
        values = set()
        for seq in seqs:
            for x in seq:
                values.add(x)  # to check the length of sequence
        G = {v: [] for v in values}
        indegree = {v: 0 for v in values}

        for seq in seqs:
            for i in range(len(seq) - 1):  # because the seq length can be any even number not only 2
                G[seq[i]].append(seq[i + 1])
                indegree[seq[i + 1]] += 1

        nonDependent = deque()
        for node in indegree:
            if indegree[node] == 0:
                nonDependent.append(node)

        res = []
        while nonDependent:
            if len(nonDependent) != 1:  # if nonDependent has more than one node, then it means there is more than one topological sorting (sequence)
                return False
            node = nonDependent.pop()
            res.append(node)
            for adjNode in G[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    nonDependent.append(adjNode)
        return len(res) == len(values) and res == org

