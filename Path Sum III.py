# https://leetcode.com/problems/path-sum-iii/
"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Brute Force
# Time: O(N^2)
# Space : O(H) where H is height of the tree
class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # define global return var
        self.numOfPaths = 0
        # 1st layer DFS to go through each node
        self.dfs(root, target)
        # return result
        return self.numOfPaths

    # define: traverse through the tree, at each treenode, call another DFS to test if a path sum include the answer
    def dfs(self, node, target):
        # exit condition
        if node is None:
            return
        # dfs break down
        self.test(node, target)  # you can move the line to any order, here is pre-order
        self.dfs(node.left, target)
        self.dfs(node.right, target)

    # define: for a given node, DFS to find any path that sum == target, if find self.numOfPaths += 1
    def test(self, node, target):
        # exit condition
        if node is None:
            return
        if node.val == target:
            self.numOfPaths += 1

        # test break down
        self.test(node.left, target - node.val)
        self.test(node.right, target - node.val)


# Better Implementation
class SolutionBruteForce(object):
    def find_paths(self, root, target):
        if root:
            return int(root.val == target) + self.find_paths(root.left, target - root.val) + self.find_paths(root.right, target - root.val)
        return 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return self.find_paths(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0


# Prefix Sum - Preorder DFS
# Time: O(N)
# Space : O(N)
class Solution:
    def pathSum(self, root: TreeNode, summ: int) -> int:
        def pathSumHelper(node, curr_sum):
            if not node:
                return
            curr_sum += node.val
            if curr_sum == self.k:
                self.count += 1
            self.count += prefix_mp[curr_sum - self.k]
            prefix_mp[curr_sum] += 1
            pathSumHelper(node.left, curr_sum)
            pathSumHelper(node.right, curr_sum)
            prefix_mp[curr_sum] -= 1

        self.count = 0
        self.k = summ
        prefix_mp = defaultdict(int)
        pathSumHelper(root, 0)
        return self.count
