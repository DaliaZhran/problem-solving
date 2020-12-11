# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Note: A leaf is a node with no children.

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

""" sol """
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # * bottom-up approach
        # * Complexity same as iterative sol
        # if root is None:
        #     return 0
        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)

        # return max(left, right) + 1

        # * top-down approach
        def maxDepthHelper(root, depth):
            if root is None:
                return
            if root.left is None and root.right is None:
                self.answer = max(self.answer, depth)
            maxDepthHelper(root.left, depth + 1)
            maxDepthHelper(root.right, depth + 1)

        self.answer = 0
        maxDepthHelper(root, 1)
        return self.answer

    # ** iterative sol
    # * Time complexity : O(N)
    # * Space complexity : in the worst case, the tree is completely unbalanced, e.g. each node has only left child node,
    # the recursion call would occur N times (the height of the tree), therefore the storage to keep the call stack would be O(N).
    # But in the average case (the tree is balanced), the height of the tree would be log(N).
    # Therefore, the space complexity in this case would be O(log(N)).
    def maxDepth(self, root):
        stack = []
        if root is not None:
            stack.append((root, 1))
        depth = 0
        while stack:
            root, curr_depth = stack.pop()
            if root is not None:
                depth = max(curr_depth, depth)
                stack.append((root.left, curr_depth + 1))
                stack.append((root.right, curr_depth + 1))
        return depth
