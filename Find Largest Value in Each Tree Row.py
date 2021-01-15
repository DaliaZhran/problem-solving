# https://leetcode.com/problems/find-largest-value-in-each-tree-row/


"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
"""
import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# BFS
# time -> O(n) n is the number of nodes
# space -> O(n/2)
class Solution(object):
    def largestValues(self, root):
        if not root:
            return []
        res = []
        queue = collections.deque([root])

        while queue:
            levelSize = len(queue)
            levelMax = queue[0].val
            for _ in range(levelSize):
                node = queue.popleft()
                levelMax = max(node.val, levelMax)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(levelMax)
        return res


# same bfs implementation without poping from the queue
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            next_level = []
            res.append(queue[0].val)
            for node in queue:
                res[-1] = max(res[-1], node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            queue = next_level
        return res


# DFS
# time : O(N)
# Space : O(H)
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
