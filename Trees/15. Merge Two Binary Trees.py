# https://leetcode.com/problems/merge-two-binary-trees/

# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

# Input:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# Output:
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Recursive
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1


# Good solution -> https://leetcode.com/problems/merge-two-binary-trees/discuss/104429/Python-BFS-Solution
class Solution(object):
    # Iterative - BFS + queue
    def mergeTrees(self, t1, t2):
        if not t1 or not t2:
            return t1 or t2

        queue = [(t1, t2)]
        while queue:
            n1, n2 = queue.pop(0)
            if n1 and n2:
                n1.val += n2.val

                if not n1.left and n2.left:
                    n1.left = TreeNode(0)
                if not n1.right and n2.right:
                    n1.right = TreeNode(0)

                queue.append((n1.left, n2.left))
                queue.append((n1.right, n2.right))

        return t1


# DFS + stack
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 or not t2:
            return t1 or t2

        queue = [(t1, t2)]
        while queue:
            n1, n2 = queue.pop()
            if n1 and n2:
                n1.val += n2.val

                # we only care about null nodes in tree1
                if not n1.left and n2.left:
                    n1.left = TreeNode(0)
                if not n1.right and n2.right:
                    n1.right = TreeNode(0)

                queue.append((n1.right, n2.right))
                queue.append((n1.left, n2.left))
        return t1
