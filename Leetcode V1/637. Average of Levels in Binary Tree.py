
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            summ = 0
            for _ in range(levelSize):
                el = queue.popleft()
                summ += el.val

                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)

            result.append(summ / float(levelSize))

        return result
