from collections import deque


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

