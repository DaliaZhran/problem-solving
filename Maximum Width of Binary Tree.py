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

# BFS
# it depends column index for each node -> left_child = parent_index * 2 and right_child = parent_index * 2 + 1
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = deque([(root, 0)])
        maxWidth = 0
        while queue:
            levelSize = len(queue)  # this also can be used  newLevel = [] or use a dummy node to separate levels
            maxWidth = max(maxWidth, queue[-1][1] - queue[0][1] + 1)  # get width from col index of the level boundaries (most left and most right)

            for _ in range(levelSize):
                node, colIndex = queue.popleft()
                if node.left:
                    queue.append((node.left, colIndex * 2))  # append left child with its column index given the parent index
                if node.right:
                    queue.append((node.right, colIndex * 2 + 1))

        return maxWidth


# DFS -> Side Effect Recursion
# time O(n)
# space -> recursion stack + dictionary -> O(n) + O(n) = O(n)
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def DFS(node, depth, colIndex):
            if not node:
                return
            if depth not in self.levelsMostLeft:
                self.levelsMostLeft[depth] = colIndex
            self.maxWidth = max(self.maxWidth, colIndex - self.levelsMostLeft[depth] + 1)
            DFS(node.left, depth + 1, colIndex * 2)
            DFS(node.right, depth + 1, colIndex * 2 + 1)

        if not root:
            return 0

        self.maxWidth = 0
        self.levelsMostLeft = {}
        DFS(root, 0, 0)
        return self.maxWidth
