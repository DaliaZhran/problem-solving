# time
# space

# Given a binary tree, return the preorder traversal of its nodes' values.

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # recursive
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def preorderTraversalHelper(root):
            if root is None:
                return

            res.append(root.val)
            if root.left:
                preorderTraversalHelper(root.left)
            if root.right:
                preorderTraversalHelper(root.right)

        res = []
        preorderTraversalHelper(root)

        return res

    # iterative
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                # order because it is stack
                stack.append(node.right)
                stack.append(node.left)
        return res
