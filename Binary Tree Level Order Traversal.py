# https://leetcode.com/problems/binary-tree-level-order-traversal/
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

import collections
from typing import List


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative
# Time : O(N) since each node is processed exactly once.
# Space : O(N)
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            res.append([])
            for _ in range(level_size):
                node = queue.popleft()
                res[-1].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


# Recursive
# Time : O(N) since each node is processed exactly once.
# Space : O(N) for output and stack
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def helper(node, level):
            if not node:
                return
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            helper(node.left, level + 1)
            helper(node.right, level + 1)

        res = []
        helper(root, 0)
        return res
