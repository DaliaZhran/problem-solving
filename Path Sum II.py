# https://leetcode.com/problems/path-sum-ii/

"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Preorder DFS
# Time : O(N)
# Space : O(N)
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def pathSumHelper(node, sum, curr_path, res):
            if node:
                if not node.left and not node.right and sum == node.val:
                    curr_path.append(node.val)
                    res.append(curr_path)
                    return
                pathSumHelper(node.left, sum - node.val, curr_path + [node.val], res)
                pathSumHelper(node.right, sum - node.val, curr_path + [node.val], res)

        res = []
        pathSumHelper(root, sum, [], res)
        return res


# check difference with the previous one
# Time : O(N^2)
# Space : O(N)
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def pathSumHelper(node, sum, curr_path, res):
            if not node:
                return
            curr_path.append(node.val)
            if not node.left and not node.right and sum == node.val:
                res.append(list(curr_path))
            else:
                pathSumHelper(node.left, sum - node.val, curr_path, res)
                pathSumHelper(node.right, sum - node.val, curr_path, res)
            curr_path.pop()  # backtrack

        res = []
        pathSumHelper(root, sum, [], res)
        return res


# DFS -> sol with no helper function
class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right and sum == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        return [[root.val] + i for i in tmp]


# DFS + stack I
class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        stack = [(root, sum - root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, val - curr.right.val, ls + [curr.right.val]))
            if curr.left:
                stack.append((curr.left, val - curr.left.val, ls + [curr.left.val]))
        return res


# DFS + stack II
class Solution(object):
    def pathSum(self, root, s):
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            curr, ls = stack.pop()
            if not curr.left and not curr.right and sum(ls) == s:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, ls + [curr.right.val]))
            if curr.left:
                stack.append((curr.left, ls + [curr.left.val]))
        return res


# BFS
# not preferred here
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = deque([(root, root.val, [root.val])])
        res = []
        while queue:
            node, curSum, path = queue.popleft()
            if not node.left and not node.right and curSum == sum:
                res.append(path)
            if node.left:
                queue.append((node.left, curSum + node.left.val, path + [node.left.val]))
            if node.right:
                queue.append((node.right, curSum + node.right.val, path + [node.right.val]))
        return res


# all solutions -> https://leetcode.com/problems/path-sum-ii/discuss/36829/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)


# https://cs.stackexchange.com/questions/83574/does-space-complexity-analysis-usually-include-output-space