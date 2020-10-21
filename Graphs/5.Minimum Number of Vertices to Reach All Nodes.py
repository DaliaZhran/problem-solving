# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

# Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi]
# represents a directed edge from node fromi to node toi.

# Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

# Notice that you can return the vertices in any order.


# Solution
"""
Intuition
Just return the nodes with no in-degres.

Explanation
Quick prove:
1 - All nodes with no in-degree must in the final result, because they can not be reached from any other nodes.
2 - All other nodes can be reached from some other nodes.

"""


class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        in_edges = [0] * n
        for src, dest in edges:
            in_edges[dest] += 1

        res = []
        for i in range(n):
            if in_edges[i] == 0:
                res.append(i)
        return res

    # nice sol - set difference
    def findSmallestSetOfVertices(self, n, edges):
        return list(set(range(n)) - set(j for i, j in edges))
