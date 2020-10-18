# https://leetcode.com/problems/find-leaves-of-binary-tree/

# Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.


# Example:

# Input: [1,2,3,4,5]

#           1
#          / \
#         2   3
#        / \
#       4   5

# Output: [[4,5,3],[2],[1]]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS (calculate the height from bottom)
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def findLeavesDFS(node):
            if not node:
                return -1
            level = 1 + max(findLeavesDFS(node.left), findLeavesDFS(node.right))

            if len(self.res) == level:
                self.res.append([])
            self.res[level].append(node.val)

            return level

        self.res = []
        findLeavesDFS(root)
        return self.res

