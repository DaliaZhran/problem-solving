# https://leetcode.com/problems/diameter-of-binary-tree/

# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS - bottom up approach
class Solution(object):
    diameter = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            # path
            self.diameter = max(self.diameter, left + right)
            # depth
            return max(left, right) + 1

        depth(root)
        return self.diameter
