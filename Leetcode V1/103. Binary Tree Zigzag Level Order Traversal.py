from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = deque()
        queue.append(root)
        leftToRight = True
        while queue:
            levelSize = len(queue)
            # result.append([])
            result.append(deque())
            for _ in range(levelSize):
                el = queue.popleft()
                if leftToRight:
                    result[-1].append(el.val)
                else:
                    result[-1].appendleft(el.val)
                    # result[-1].insert(0, el.val)

                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            leftToRight = not leftToRight
            # result.append(currentLevel)

        return result
