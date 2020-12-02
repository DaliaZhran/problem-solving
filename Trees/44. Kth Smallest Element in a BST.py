# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # In Order Traversal
        def inOrderTraversal(root):
            if root:
                return inOrderTraversal(root.left) + [root.val] + inOrderTraversal(root.right)
            else:
                return []

        return inOrderTraversal(root)[k - 1]


# Normal Inorder traversal
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # In Order Traversal
        inorder = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            inorder.append(curr.val)
            curr = curr.right
        return inorder[k - 1]


# Optimized Inorder Traversal
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # In Order Traversal
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if k == 1:
                return root.val
            root = root.right
            k -= 1


# good implementation
class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        for val in self.inorder(root):
            if k == 1:
                return val
            else:
                k -= 1

    def inorder(self, root):
        if root is not None:
            for val in self.inorder(root.left):
                yield val
            yield root.val
            for val in self.inorder(root.right):
                yield val