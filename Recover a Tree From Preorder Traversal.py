# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative
# time -> O(N)
# space -> O(N)
class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        stack, i = [], 0
        while i < len(S):
            level, val = 0, ""
            # calculate the level
            while i < len(S) and S[i] == "-":
                level, i = level + 1, i + 1
            # get the value of node
            while i < len(S) and S[i] != "-":
                val, i = val + S[i], i + 1
            # leave only the parent of the current node in the stack
            while len(stack) > level:
                stack.pop()
            node = TreeNode(val)
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
