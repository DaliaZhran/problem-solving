# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
"""
import collections
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Iterative
# Time : O(N) since each node is processed exactly once.
# Space : O(N)
class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
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
                # queue.extend(node.children) # instead of for loop
                for child in node.children:
                    queue.append(child)
        return res


# Recursive
# Time : O(N) since each node is processed exactly once.
# Space : O(log N) average case, O(N) worst case. The space used is on the runtime stack.
class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        def helper(node, level):
            if len(res) == level:
                res.append([node.val])
            else:
                res[level].append(node.val)

            for child in node.children:
                helper(child, level + 1)

        if not root:
            return []
        res = []
        return helper(root, 0)
