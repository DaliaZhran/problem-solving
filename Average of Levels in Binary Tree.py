# https://leetcode.com/problems/average-of-levels-in-binary-tree/

"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
"""
import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS
# Time : O(N)
# Space: O(N)
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        res = []
        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            res.append(0)
            for _ in range(level_size):
                node = queue.popleft()
                res[-1] += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res[-1] /= level_size
        return res


# DFS
# Time : O(N)
# Space: O(N)
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        def helper(node, level):
            if not node:
                return

            if len(res) == level:
                res.append([node.val, 1])
            else:
                res[level][0] += node.val
                res[level][1] += 1

            helper(node.left, level + 1)
            helper(node.right, level + 1)

        res = []
        helper(root, 0)
        return [summ / count for summ, count in res]
