from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        minDepth = 0
        while queue:
            levelSize = len(queue)
            minDepth += 1
            for i in range(levelSize):
                el = queue.popleft()
                if not el.left and not el.right:
                    return minDepth

                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
