# https://leetcode.com/problems/graph-valid-tree/


"""
Note :
For the graph to be a valid tree, it must have exactly n - 1 edges. Any less, and it can't possibly be fully connected. Any more, and it has to contain cycles. Additionally, if the graph is fully connected and contains exactly n - 1 edges, it can't possibly contain a cycle, and therefore must be a tree!
"""
# We deal with it as an undirected graph and try to detect cycles
# Time : O(N + E) -> O(N)
# Space : O(N + E) -> O(N)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = [[] for _ in range(n)]
        for f, t in edges:
            graph[f].append(t)
            graph[t].append(f)

        parent = {0: -1}
        stack = [0]
        while stack:
            node = stack.pop()
            for nei in graph[node]:
                if nei == parent[node]:
                    continue
                if nei in parent:
                    return False
                parent[nei] = node
                stack.append(nei)

        return len(parent) == n


# Time : O(N + E) -> O(N)
# Space : O(N + E) -> O(N)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = [[] for _ in range(n)]
        for f, t in edges:
            graph[f].append(t)
            graph[t].append(f)

        seen = {0}  # to detect cycles
        stack = [0]

        while stack:
            node = stack.pop()
            for nei in graph[node]:
                if nei in seen:
                    continue
                seen.add(nei)
                stack.append(nei)

        # make sure all nodes are connected and no cycles exist
        return len(seen) == n
