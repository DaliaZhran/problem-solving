# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
"""
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi]
represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.
"""

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
        indegree = [0] * n
        for source, dest in edges:
            indegree[dest] += 1

        return [index for index, x in enumerate(indegree) if x == 0]

    # nice sol - set difference
    def findSmallestSetOfVertices(self, n, edges):
        return list(set(range(n)) - set(j for i, j in edges))
