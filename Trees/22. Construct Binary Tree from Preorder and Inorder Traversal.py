# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
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


# recursive
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def buildTreePreIn(preStart, inStart, inEnd):
            if inStart > inEnd or preStart > len(preorder) - 1:
                return None

            root = TreeNode(preorder[preStart])
            inIndex = inorder.index(root.val)

            root.left = buildTreePreIn(preStart + 1, inStart, inIndex - 1)
            root.right = buildTreePreIn(preStart + (inIndex - inStart) + 1, inIndex + 1, inEnd)

            return root

        return buildTreePreIn(0, 0, len(inorder))

