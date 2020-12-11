# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level X such that the sum of all the values of nodes at level X is maximal.


from collections import deque


# BFS
# time -> O(n)
# space -> O(n/2)
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        queue = deque([root])
        maxLevel = [1, root.val]
        level = 0
        while queue:
            # levelSum = sum([n.val for n in queue])
            levelSum = 0
            levelSize = len(queue)
            level += 1
            for _ in range(levelSize):
                node = queue.popleft()
                levelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if maxLevel[-1] < levelSum:
                maxLevel = [level, levelSum]

        return maxLevel[0]


# DFS
# time -> O(n)
# space -> O(n)
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def maxLevelSumHelper(node, level):
            if not node:
                return
            if level == len(self.sums):
                self.sums.append(node.val)
            else:
                self.sums[level] += node.val

            maxLevelSumHelper(node.left, level + 1)
            maxLevelSumHelper(node.right, level + 1)

        self.sums = []
        maxLevelSumHelper(root, 0)
        return 1 + self.sums.index(max(self.sums))


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
