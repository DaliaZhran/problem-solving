# https://leetcode.com/problems/smallest-string-starting-from-leaf/

# Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.

# Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

# (As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)


# BFS
# Time Complexity: O(N)
# Space Complexity: O(N) worst and O(log N) average
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        res = 8500 * "z"  # largest possible string (problem parameters)
        chrs = "abcdefghijklmnopqrstuvwxyz"
        stack = [(root, "")]
        while len(stack) > 0:
            node, path = stack.pop()
            cur = chrs[node.val]
            if node.left == None and node.right == None:
                res = min(res, cur + path)
            if node.left != None:
                stack.append((node.left, cur + path))
            if node.right != None:
                stack.append((node.right, cur + path))
        return res


# DFS
# Time Complexity: O(N)
# Space Complexity: O(N) worst and O(log N) average
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.alpha = "abcdefghijklmnopqrstuvwxyz"
        self.min = 8500 * "z"

        def smallestFromLeafHelper(node, path):
            if not node:
                return
            path = self.alpha[node.val] + path
            if not node.left and not node.right and path < self.min:
                self.min = path
            smallestFromLeafHelper(node.left, path)
            smallestFromLeafHelper(node.right, path)

        smallestFromLeafHelper(root, "")
        return self.min
