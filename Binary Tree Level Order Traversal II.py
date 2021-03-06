# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections
from typing import List


# Iterative
# Time : O(N) since each node is processed exactly once.
# Space : O(N)
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
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
        return res[::-1]


# Iterative -> No reversing
# Time : O(N) since each node is processed exactly once.
# Space : O(N)
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = collections.deque()
        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            res.appendleft([])  # appendleft in deque is O(1), same as linkedlist
            for _ in range(level_size):
                node = queue.popleft()
                res[0].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


# Time : O(N)
# Space : O(N)
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def helper(node, level):
            if not node:
                return node
            if len(res) == level:
                res.appendleft([])
            res[len(res) - level - 1].append(node.val)  # to avoid reversing at the end
            helper(node.left, level + 1)
            helper(node.right, level + 1)

        res = collections.deque()
        helper(root, 0)
        return res
