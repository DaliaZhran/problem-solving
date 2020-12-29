# https://leetcode.com/problems/distribute-coins-in-binary-tree/

# good sol -> https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221939/C%2B%2B-with-picture-post-order-traversal
# diff sol -> https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221930/JavaC%2B%2BPython-Recursive-Solution

"""
Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
# every node should have a value of 1 (since there is N nodes and N coins in total), so any difference that is not 1 should be counted as a move.
# This is done recursively in a bottom up approach
class Solution(object):
    ans = 0

    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def distributeCoinsDFS(node):
            if not node:
                return 0
            left = distributeCoinsDFS(node.left)
            right = distributeCoinsDFS(node.right)
            self.ans += abs(left) + abs(right)

            return node.val + left + right - 1

        distributeCoinsDFS(root)
        return self.ans
