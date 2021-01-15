# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

from collections import deque

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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = collections.deque([root])
        left_to_right = 1
        while queue:
            level_size = len(queue)
            res.append(deque())
            for _ in range(level_size):
                node = queue.popleft()
                if left_to_right:
                    res[-1].append(node.val)
                else:
                    res[-1].appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            left_to_right ^= 1

        return res


# Recursive
# Time : O(N) since each node is processed exactly once.
# Space Complexity : O(H), where H is the height of the tree, i.e. the number of levels in the tree, which would be roughly log2(N)
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def helper(node, level, res):
            if not node:
                return []
            if len(res) == level:
                res.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    res[level].append(node.val)
                else:
                    res[level].appendleft(node.val)

            helper(node.left, level + 1, res)
            helper(node.right, level + 1, res)

            return res

        res = []
        return helper(root, 0, [])