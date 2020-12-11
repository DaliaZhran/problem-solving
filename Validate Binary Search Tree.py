# time
# space

# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Input: [2,1,3]
# Output: true


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive - DFS
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isValidBSTHelper(root, lower=float("-inf"), upper=float("inf")):
            if root is None:
                return True
            val = root.val
            if val <= lower or val >= upper:  # the equal is important
                return False
            return isValidBSTHelper(root.left, lower, val) and isValidBSTHelper(root.right, val, upper)

        return isValidBSTHelper(root)
