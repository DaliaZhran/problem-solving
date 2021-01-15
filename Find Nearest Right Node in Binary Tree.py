# https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/

"""
Given the root of a binary tree and a node u in the tree, return the nearest node on the same level that is to the right of u, or return null if u is the rightmost node in its level.
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS
# time -> O(N)
# space -> O(N/2) -> O(N)
class Solution(object):
    def findNearestRightNode(self, root, u):
        """
        :type root: TreeNode
        :type u: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return []
        curr_level = deque([root])
        while curr_level:
            next_level = deque()
            while curr_level:
                node = curr_level.popleft()
                if node is u:
                    return None if not curr_level else curr_level[0]
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            curr_level = next_level

        return None


class Solution(object):
    def findNearestRightNode(self, root, u):
        """
        :type root: TreeNode
        :type u: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        queue = deque([root])

        while queue:
            levelSize = len(queue)
            for i in range(levelSize):
                node = queue.popleft()
                if u is node and i != levelSize - 1:
                    # return queue.popleft()
                    return queue[0]
                elif u is node and i == levelSize - 1:
                    return None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return None


# DFS
# Time : O(N)
# Space : O(H)
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        def dfs(current_node, depth):
            nonlocal u_depth, next_node
            # the depth to look for next node is identified
            if current_node == u:
                u_depth = depth
                return
            # we're on the level to look for the next node
            if depth == u_depth:
                # if this next node is not identified yet
                if next_node is None:
                    next_node = current_node
                return
            # continue to traverse the tree
            if current_node.left:
                dfs(current_node.left, depth + 1)
            if current_node.right:
                dfs(current_node.right, depth + 1)

        u_depth, next_node = -1, None
        dfs(root, 0)
        return next_node