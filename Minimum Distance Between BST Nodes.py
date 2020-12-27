# https://leetcode.com/problems/minimum-distance-between-bst-nodes
"""
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Inorder Traversal, then get the min diff using loop
# time -> O(n)
# space -> O(n)
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def inOrderTraversal(node):
            return inOrderTraversal(node.left) + [node.val] + inOrderTraversal(node.right) if node else []

        nums = inOrderTraversal(root)
        return min(nums[i + 1] - nums[i] for i in xrange(len(nums) - 1))


# Inorder Traversal, not required to loop to get min
# time -> O(n)
# space -> O(H) -> recursive Stack
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def inOrderTraversal(node):
            if node:
                inOrderTraversal(node.left)
                self.ans = min(self.ans, node.val - self.prev)
                self.prev = node.val
                inOrderTraversal(node.right)

        self.ans = float("inf")
        self.prev = float("-inf")
        inOrderTraversal(root)
        return self.ans


# different implementation for the prev sol -> no helper function
class Solution(object):
    min_diff = float("inf")
    prev = float("-inf")  # -inf because we subtract it from the current node (to avoid having -inf as min)

    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        self.min_diff = min(self.min_diff, root.val - self.prev)
        self.prev = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.min_diff