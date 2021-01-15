# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children # children is []
"""

# recursive
# * Time complexity : O(N).
# * Space complexity : O(N) worst case if tree is unbalanced and O(log N) average.
class Solution:
    def maxDepth(self, root: "Node") -> int:
        def maxDepthHelper(node, depth):
            if not node:
                return 0
            if depth > self.max_depth:
                self.max_depth = depth
            for child in node.children:
                maxDepthHelper(child, depth + 1)

        self.max_depth = 0
        maxDepthHelper(root, 1)
        return self.max_depth


# iterative DFS
# * Time complexity : O(N).
# * Space complexity : O(N).
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        answer = 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if not node.children:
                answer = max(answer, depth)
            else:
                for child in node.children:
                    stack.append((child, depth + 1))

        return answer
