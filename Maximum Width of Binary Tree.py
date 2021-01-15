# https://leetcode.com/problems/maximum-width-of-binary-tree/

# Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

# It is guaranteed that the answer will in the range of 32-bit signed integer.

# Input:

#            1
#          /   \
#         3     2
#        / \     \
#       5   3     9

# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).


from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Intuitive BFS - Time Limit Exceeded
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = deque([root])
        max_width = 0
        while stack:
            next_level = []
            # remove all none nodes at the end of the level
            while stack and not stack[-1]:
                stack.pop()
            # remove all none nodes at the beginning of the level
            while stack and not stack[0]:
                stack.pop(0)
            # update max_width
            max_width = max(max_width, len(stack))
            for node in stack:
                if node:
                    next_level.append(node.left)
                    next_level.append(node.right)
                else:
                    # we need to keep track of the none nodes in between our first and last not None nodes
                    next_level.append(None)
                    next_level.append(None)
            stack = next_level
        return max_width


# BFS
# it depends column index for each node -> left_child = parent_index * 2 and right_child = parent_index * 2 + 1
# Time : O(N)
# Space -> O(N/2)
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        curr_level = deque([(root, 1)])
        max_width = 0
        while curr_level:
            next_level = []
            # get width from order of the level boundaries (most left and most right)
            max_width = max(max_width, curr_level[-1][1] - curr_level[0][1] + 1)
            for node, curr_order in curr_level:
                if node.left:
                    # append left child with its order given the parent index
                    next_level.append((node.left, 2 * curr_order))
                if node.right:
                    next_level.append((node.right, 2 * curr_order + 1))
            curr_level = next_level
        return max_width


# DFS -> Side Effect Recursion
# time O(n)
# space -> recursion stack + dictionary -> O(n) + O(n) = O(n)
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def DFS(node, level, order):
            if not node:
                return
            if level not in self.levels_most_left:
                self.levels_most_left[level] = order
            self.max_width = max(self.max_width, order - self.levels_most_left[level] + 1)
            DFS(node.left, level + 1, order * 2)
            DFS(node.right, level + 1, order * 2 + 1)

        if not root:
            return 0

        self.max_width = 0
        self.levels_most_left = {}
        DFS(root, 0, 1)
        return self.max_width
