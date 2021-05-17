# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

"""
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.
"""
from collections import defaultdict, deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS
# time: O(N + K * N/K log N/K) -> K = number of cols
# space: O(N)
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        queue = deque([(root, 0, 0)])
        res_map = defaultdict(list)
        min_col, max_col = 0, 0
        while queue:
            node, row, col = queue.popleft()
            if node:
                min_col, max_col = min(col, min_col), max(col, max_col)
                res_map[col].append((row, node.val))

                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))

        res = []
        for column in range(min_col, max_col + 1):
            res_map[column].sort()
            res.append([val for r, val in res_map[column]])
        return res


# DFS
# time: O(N + K * N/K log N/K) -> K = number of cols
# space: O(N)
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        column_table = defaultdict(list)
        min_column = max_column = 0

        def DFS(node, row, column):
            if node is not None:
                nonlocal min_column, max_column
                column_table[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        DFS(root, 0, 0)

        # order by column and sort by row
        ret = []
        for col in range(min_column, max_column + 1):
            column_table[col].sort()
            col_vals = [val for row, val in column_table[col]]
            ret.append(col_vals)

        return ret
