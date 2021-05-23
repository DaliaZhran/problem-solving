# https://leetcode.com/problems/validate-binary-search-tree/

"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: [2,1,3]
Output: true
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive Preorder with Valid Range -> compare relationships between nodes
# Time : O(N)
# Space : O(H)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float("-inf"), upper=float("inf")):
            if node is None:
                return True
            if lower >= node.val or upper <= node.val:  # the equal is important
                return False
            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)

        return helper(root)


# Iterative Traversal with Valid Range
# Time : O(N)
# Space : O(N)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, -float("inf"), float("inf"))]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True


# Recusrive Inorder Traversal
# Time : O(N)
# Space : O(H)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root):
            if not root:
                return True
            if inorder(root.left) is False:
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = float("-inf")
        return inorder(root)


# Iterative Inorder Traversal
# Time : O(N)
# Space : O(N)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], float("-inf")

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True
