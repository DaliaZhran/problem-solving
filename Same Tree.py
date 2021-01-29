# https://leetcode.com/problems/same-tree/

"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion
# Time: O(N) where N is the number of nodes
# Space: O(H)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False


# Shorter Implementation
def isSameTree1(self, p, q):
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    else:
        return p == q


# Iteration
# Time: O(N) where N is the number of nodes of a tree
# Space: O(H)
# BFS maybe somtimes better in time performace so we can replace the stack with a queue (depending on the trees)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if not self.isEqual(n1, n2):
                return False
            if n1:
                stack.append((n1.left, n2.left))
                stack.append((n1.right, n2.right))

        return True

    def isEqual(self, n1, n2):
        if not n1 and not n2:
            return True
        elif not n1 or not n2:
            return False

        if n1.val == n2.val:
            return True
        return Falses