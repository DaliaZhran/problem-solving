# https://leetcode.com/problems/longest-univalue-path/

# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

# The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive
# time -> O(n)
# space -> O(H)
# the idea -> we take a bottom-up approach and compare each node with its children and take the max len path and continue to the its parent and so on.
# good explaination -> https://leetcode.com/problems/longest-univalue-path/discuss/108155/C%2B%2B-DFS-with-explanation
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def longestUnivaluePathDFS(node):
            if not node:
                return 0
            left_length = longestUnivaluePathDFS(node.left)
            right_length = longestUnivaluePathDFS(node.right)
            left_edges = right_edges = 0  # if the values of the node and its children are not equal, then the lengths will stay 0
            if node.left and node.left.val == node.val:
                left_edges = left_length + 1
            if node.right and node.right.val == node.val:
                right_edges = right_length + 1
            self.ans = max(self.ans, left_edges + right_edges)

            return max(left_edges, right_edges)

        self.ans = 0
        longestUnivaluePathDFS(root)
        return self.ans
