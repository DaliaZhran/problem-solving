# https://leetcode.com/problems/binary-tree-maximum-path-sum/

"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]

       1
      / \
     2   3

Output: 6
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# the sum can be the left or right substree or parts of the 2, so we need to get the max path sum including and excluding the root
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def maxPath(node):
            if not node:
                return 0
            left = max(maxPath(node.left), 0)  # max to avoid -ve path sum
            right = max(maxPath(node.right), 0)

            curSum = node.val + left + right
            self.max = max(self.max, curSum)

            return node.val + max(left, right)  # handles the case that the current node is not in the path

        self.max = float("-inf")
        maxPath(root)
        return self.max


# good explaination -> https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram


class Solution:
    result = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxPathSumHelper(node):
            if not node:
                return 0
            left = maxPathSumHelper(node.left)
            right = maxPathSumHelper(node.right)

            # max of the left and right subtrees
            max_child = max(left, right)
            # max of the subtrees + node and node value itself
            max_single_path = max(max_child + node.val, node.val)
            # max of a signle path inlcuding node and both subtrees + node
            max_all = max(max_single_path, left + right + node.val)

            self.result = max(self.result, max_all)
            return max_single_path

        maxPathSumHelper(root)
        return self.result
