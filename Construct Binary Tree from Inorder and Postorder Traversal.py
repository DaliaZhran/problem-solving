# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        def buildTreeHelper(postStart, inStart, inEnd):
            if postStart < 0 or inStart > inEnd:
                return None

            root = TreeNode(postorder[postStart])
            inIndex = inorder.index(root.val)

            root.left = buildTreeHelper(postStart - (inEnd - inIndex) - 1, inStart, inIndex - 1)
            root.right = buildTreeHelper(postStart - 1, inIndex + 1, inEnd)
            return root

        return buildTreeHelper(len(postorder) - 1, 0, len(inorder) - 1)

