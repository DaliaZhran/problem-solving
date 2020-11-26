# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs solution -> good space complexity
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = maxDepth(root)
        return recursiveSum(root, depth)


def recursiveSum(node, d):
    if node == None:
        return 0
    if d == 1:
        return node.val
    return recursiveSum(node.left, d - 1) + recursiveSum(node.right, d - 1)


def maxDepth(node):
    if node == None:
        return 0
    return max(maxDepth(node.left), maxDepth(node.right)) + 1
