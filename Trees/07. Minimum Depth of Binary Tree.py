# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        return left + right + 1 if left == 0 or right == 0 else min(left, right) + 1

    # BFS
    def minDepth(self, root):
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                # we are using a Level traversal so once we find the first leaf, it will be the shortest path
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))

