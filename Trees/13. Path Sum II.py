# https://leetcode.com/problems/path-sum-ii/

# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS + Queue
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = deque([(root, root.val, [root.val])])
        res = []

        while queue:
            node, curSum, path = queue.popleft()
            if not node.left and not node.right and curSum == sum:
                res.append(path)
            if node.left:
                queue.append((node.left, curSum + node.left.val, path + [node.left.val]))
            if node.right:
                queue.append((node.right, curSum + node.right.val, path + [node.right.val]))

        return res


    # DFS
    def pathSum(self, root, sum):
        res = []
        self.dfs(root, sum, [], res)
        return res
        
    def dfs(self, root, sum, ls, res):
        if root:
			if not root.left and not root.right and sum == root.val:
				ls.append(root.val)
				res.append(ls)
            self.dfs(root.left, sum-root.val, ls+[root.val], res)
            self.dfs(root.right, sum-root.val, ls+[root.val], res)


    # DFS -> sol with no helper function
    def pathSum2(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right and sum == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        return [[root.val] + i for i in tmp]


    # DFS + stack I  
    def pathSum4(self, root, sum): 
        if not root:
            return []
        res = []
        stack = [(root, sum-root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, val-curr.right.val, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
        return res 
    
    # DFS + stack II   
    def pathSum5(self, root, s): 
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            curr, ls = stack.pop()
            if not curr.left and not curr.right and sum(ls) == s:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, ls+[curr.left.val]))
        return res

# all solutions -> https://leetcode.com/problems/path-sum-ii/discuss/36829/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)
# check diff between -ve & +ve (top down vs bottom up)
