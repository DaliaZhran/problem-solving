# https://leetcode.com/problems/range-sum-of-bst/

"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
The binary search tree is guaranteed to have unique values.

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Inorder Traversal
# Time : O(N)
# Space : O(H)
class Solution(object):
    sum = 0

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        if root.left:
            self.rangeSumBST(root.left, L, R)
        if root.val >= L and root.val <= R:
            self.sum += root.val
        if root.right:
            self.rangeSumBST(root.right, L, R)
        return self.sum


# Preorder Traversal
# Time : O(N)
# Space : O(H)
class Solution:
    def rangeSumBST(self, node: TreeNode, low: int, high: int) -> int:
        if not node:
            return 0
        if node.val >= low and node.val <= high:
            return node.val + self.rangeSumBST(node.left, low, high) + self.rangeSumBST(node.right, low, high)

        return self.rangeSumBST(node.left, low, high) + self.rangeSumBST(node.right, low, high)


# getting adv of BST and check for boundaries and Divide
# Time: O(n)
# space: O(H)
class Solution(object):
    sum = 0

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        def rangeSumBSTHelper(root):
            if not root:
                return 0
            if root.val >= L and root.val <= R:
                self.sum += root.val
            if root.val < L:
                rangeSumBSTHelper(root.right)
            elif root.val > R:
                rangeSumBSTHelper(root.left)
            else:
                rangeSumBSTHelper(root.left)
                rangeSumBSTHelper(root.right)

        if not root:
            return 0
        rangeSumBSTHelper(root)

        return self.sum


class Solution:
    def rangeSumBST(self, node: TreeNode, low: int, high: int) -> int:
        if not node:
            return 0
        if node.val >= low and node.val <= high:
            return node.val + self.rangeSumBST(node.left, low, high) + self.rangeSumBST(node.right, low, high)
        elif node.val < low:
            return self.rangeSumBST(node.right, low, high)
        elif node.val > high:
            return self.rangeSumBST(node.left, low, high)

        return self.rangeSumBST(node.left, low, high) + self.rangeSumBST(node.right, low, high)