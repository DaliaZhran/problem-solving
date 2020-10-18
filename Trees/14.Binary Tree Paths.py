# https://leetcode.com/problems/binary-tree-paths/

# Given a binary tree, return all root-to-leaf paths.

# Note: A leaf is a node with no children.

# Example:

# Input:

#    1
#  /   \
# 2     3
#  \
#   5

# Output: ["1->2->5", "1->3"]

# Explanation: All root-to-leaf paths are: 1->2->5, 1->3


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# * Time complexity : O(N) since each node is visited exactly once.
# * Space complexity : O(N) as we could keep up to the entire tree.
class Solution(object):
    # BFS + Queue
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        queue = [(root, str(root.val))]
        res = []

        while queue:
            node, path = queue.pop(0)
            if not node.left and not node.right:
                res.append(path)
            if node.left:
                queue.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                queue.append((node.right, path + "->" + str(node.right.val)))
        return res


# DFS
# * Time complexity : O(N)
# * Space complexity : O(N) worst case if tree is unbalanced and O(log N) in the best case
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        self.res = []

        def dfs(node, path):
            if not node.left and not node.right:
                self.res.append(path)
            if node.left:
                dfs(node.left, path + "->" + str(node.left.val))
            if node.right:
                dfs(node.right, path + "->" + str(node.right.val))

        dfs(root, str(root.val))
        return self.res
