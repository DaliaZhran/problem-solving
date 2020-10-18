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


# time -> O(N)
# space -> O(N/2) -> O(N)
class Solution(object):
    def findNearestRightNode(self, root, u):
        """
        :type root: TreeNode
        :type u: TreeNode
        :rtype: TreeNode
        """
        # BFS
        if not root:
            return root
        queue = deque([root])

        while queue:
            newLevel = deque()
            while queue:
                node = queue.popleft()
                if u is node and queue:
                    # return queue.popleft()
                    return queue[0]  # better time but worse space (in terms of leetcode)
                elif u is node and not queue:
                    return None
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)
            queue = newLevel
        return None


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findNearestRightNode(self, root, u):
        """
        :type root: TreeNode
        :type u: TreeNode
        :rtype: TreeNode
        """
        # BFS
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
