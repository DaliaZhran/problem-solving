"""
Initialize an empty stack for storage of nodes, S.
For each vertex u, define u.visited to be false.
Push the root (first node to be visited) onto S.
While S is not empty:
    Pop the first element in S, u.
    If u.visited = false, then:
        U.visited = true
        for each unvisited neighbor w of u:
            Push w into S.
End process when all nodes have been visited.
"""

## we use visited for graphs
# def depth_first_search(graph):
#     visited, stack = set(), [root]
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#             stack.extend(graph[vertex] - visited)
#     return visited


# def depth_first_search_recursive(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     for next in graph[start] - visited:
#         depth_first_search_recursive(graph, next, visited)
#     return visited


def maxLevelSum(self, root):
    """
        :type root: TreeNode
        :rtype: int
        """

    def maxLevelSumHelper(node, level):
        if not node:
            return
        if level == len(self.sums):
            self.sums.append(node.val)
        else:
            self.sums[level] += node.val

        maxLevelSumHelper(node.left, level + 1)
        maxLevelSumHelper(node.right, level + 1)

    self.sums = []
    maxLevelSumHelper(root, 0)
    return 1 + self.sums.index(max(self.sums))
