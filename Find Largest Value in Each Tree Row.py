# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# time -> O(n) n is the number of nodes
# space -> O(n/2)

# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# BFS
class Solution(object):
    def largestValues(self, root):
        if not root:
            return []
        res = []
        queue = collections.deque([root])

        while queue:
            levelSize = len(queue)
            levelMax = queue[0].val
            for i in range(levelSize):
                node = queue.popleft()
                levelMax = max(node.val, levelMax)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(levelMax)
        return res


# DFS -> nice to know sol
class Solution(object):
    def largestValues(self, root):
        self.ans = []
        self.helper(root, 0)
        return self.ans

    def helper(self, node, level):
        if not node:
            return
        if len(self.ans) == level:
            self.ans.append(node.val)
        else:
            self.ans[level] = max(self.ans[level], node.val)
        self.helper(node.left, level + 1)
        self.helper(node.right, level + 1)

