# https://leetcode.com/problems/symmetric-tree/
import collections


# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3


# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3


# Follow up: Solve it both recursively and iteratively.


# run time is O(n)
# Space is O(n)
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isMirror(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2 or n1.val != n2.val:
                return False

            return isMirror(n1.left, n2.right) and isMirror(n1.right, n2.left)

        if not root:
            return True
        return isMirror(root.left, root.right)

    # BFS
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = collections.deque([root, root])
        while queue:
            n1, n2 = queue.popleft(), queue.popleft()
            if not n1 and not n2:
                continue
            if not n1 or not n2 or n1.val != n2.val:
                return False
            queue.append(n1.left)
            queue.append(n2.right)
            queue.append(n1.right)
            queue.append(n2.left)

        return True
