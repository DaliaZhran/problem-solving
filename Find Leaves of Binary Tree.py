# https://leetcode.com/problems/find-leaves-of-binary-tree/
"""
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.


# Example:

# Input: [1,2,3,4,5]

#           1
#          / \
#         2   3
#        / \
#       4   5

# Output: [[4,5,3],[2],[1]]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Postorder DFS (calculate the height from bottom)
# Time : O(N)
# Space : O(H) where H is height of the tree
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def helper(node, res):
            if not node:
                return -1
            left = helper(node.left, res)
            right = helper(node.right, res)
            level = 1 + max(left, right)

            if len(res) == level:
                res.append([])
            res[level].append(node.val)

            return level

        res = []
        helper(root, res)
        return res


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def postorder(node):
            if not node:
                return 0
            left = postorder(node.left)
            right = postorder(node.right)
            if len(res) == max(left, right):
                res.append([])
            res[max(left, right)].append(node.val)
            return max(left, right) + 1

        res = []
        postorder(root)
        return res
