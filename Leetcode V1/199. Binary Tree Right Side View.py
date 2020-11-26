from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            for i in range(levelSize):
                el = queue.popleft()
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            result.append(el.val)

        return result
