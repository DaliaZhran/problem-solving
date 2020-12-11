# https://leetcode.com/problems/find-all-the-lonely-nodes/

# In a binary tree, a lonely node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node.

# Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. Return the list in any order.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS + stack
# time: O(n)
# memory: O(n)
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left and node.right:
                stack.append(node.left)
                stack.append(node.right)
            elif node.left and not node.right:
                res.append(node.left.val)
                stack.append(node.left)
            elif not node.left and node.right:
                res.append(node.right.val)
                stack.append(node.right)

        return res


# DFS + recursive
# time: O(n)
# memory: O(1) ignoring res memory and used stack for recursion, otherwise it is O(n)
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def getLonelyNodesHelper(node):
            if not node:
                return
            if node.left and node.right:
                getLonelyNodesHelper(node.left)
                getLonelyNodesHelper(node.right)
            elif node.left and not node.right:
                self.res.append(node.left.val)
                getLonelyNodesHelper(node.left)
            elif not node.left and node.right:
                self.res.append(node.right.val)
                getLonelyNodesHelper(node.right)

        self.res = []
        getLonelyNodesHelper(root)
        return self.res


# DFS + recursive + top down approach
# time: O(n)
# memory: O(1) ignoring res memory and used stack for recursion, otherwise it is O(n)
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def getLonelyNodesHelper(node, isLonely):
            if not node:
                return
            if isLonely:
                self.res.append(node.val)

            getLonelyNodesHelper(node.left, node.right is None)
            getLonelyNodesHelper(node.right, node.left is None)

        self.res = []
        getLonelyNodesHelper(root, False)
        return self.res
