# https://leetcode.com/problems/closest-binary-search-tree-value/
"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# recursive approach
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def closestValueHelper(root):
            if not root:
                return
            if abs(target - root.val) < abs(target - self.closest):
                self.closest = root.val
            if root.val < target:
                closestValueHelper(root.right)
            else:
                closestValueHelper(root.left)

        self.closest = root.val
        closestValueHelper(root)
        return self.closest


# iterative
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key=lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest