# https://leetcode.com/problems/path-sum/
"""
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

# DFS or Recursive -> top down approach
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        def hasPathSumHelper(root, targetSum, currentSum):
            if not root:
                return False
            currentSum += root.val
            if not root.left and not root.right and currentSum == targetSum:
                return True
            return hasPathSumHelper(root.left, targetSum, currentSum) or hasPathSumHelper(root.right, targetSum, currentSum)

        return hasPathSumHelper(root, sum, 0)


# DFS or Recursive -> different implementation with no helper function
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and sum - root.val == 0:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


# DFS with stack
class Solution(object):
    def hasPathSum(self, root, sum):
        stack = [(root, sum)]
        while stack:
            root, currentSum = stack.pop()
            if root:
                if not root.right and not root.left and root.val == currentSum:
                    return True
                stack.append((root.right, currentSum - root.val))
                stack.append((root.left, currentSum - root.val))

        return False


# BFS Solution - same idea as dfs since we visit all nodes and check sum at all leaves until we reach the target
# DFS is usually better since we can reach faster than BFS
class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        queue = [(root, sum - root.val)]
        while queue:
            curr, val = queue.pop(0)
            if not curr.left and not curr.right and val == 0:
                return True
            if curr.left:
                queue.append((curr.left, val - curr.left.val))
            if curr.right:
                queue.append((curr.right, val - curr.right.val))
        return False


# https://leetcode.com/problems/path-sum/discuss/36486/Python-solutions-(DFS-recursively-DFS%2Bstack-BFS%2Bqueue)