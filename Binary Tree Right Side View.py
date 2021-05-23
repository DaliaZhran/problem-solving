# https://leetcode.com/problems/binary-tree-right-side-view/
"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""


from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative BFS
# Time complexity: O(N) since one has to visit each node.
# Space complexity: O(D) to keep the queues, where D is a tree diameter. Let's use the last level to estimate the queue size.
# This level could contain up to N/2 tree nodes in the case of complete binary tree.
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(node.val)
        return res


# DFS
# Time complexity: O(N) since one has to visit each node.
# Space complexity: O(H) to keep the recursion stack, where H is a tree height. The worst-case situation is a skewed tree, when H = N
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def helper(node, answer, level):
            if not node:
                return None
            if level == len(answer):
                answer.append(node.val)

            helper(node.right, answer, level + 1)  # we start going through all right children first
            helper(node.left, answer, level + 1)

        answer = []
        helper(root, answer, 0)
        return answer


# Good Article -> https://leetcode.com/problems/binary-tree-right-side-view/solution/
