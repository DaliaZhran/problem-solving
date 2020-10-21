# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level X such that the sum of all the values of nodes at level X is maximal.


# Time Complexity: O(N)
# Space Complexity: O(N) because of stack call
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level_sums = {}

        def maxLevelSumDFS(node, level):
            if not node:
                return

            maxLevelSumDFS(node.left, level + 1)
            level_sums[level] = node.val + level_sums.get(level, 0)
            maxLevelSumDFS(node.right, level + 1)

        maxLevelSumDFS(root, 1)

        return max(level_sums, key=level_sums.get)  # returns key and compares values
