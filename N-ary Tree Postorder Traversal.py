# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Follow up:

Recursive solution is trivial, could you do it iteratively?
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Recursive DFS
# Time O(N) where N is the number of nodes
# Space O(H) where H is the height of the tree
class Solution:
    def postorder(self, root: "Node") -> List[int]:
        def helper(node, result):
            for child in node.children:
                helper(child, result)
            result.append(node.val)

        if not root:
            return []
        res = []
        helper(root, res)
        return res


# Iterative DFS - reverse preorder
# Time O(N) where N is the number of nodes
# Space O(N)
class Solution:
    def postorder(self, root: "Node") -> List[int]:
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                for child in node.children:
                    stack.append(child)
        return result[::-1]


# Iterative DFS - same idea as binary tree postorder
# Time O(N) where N is the number of nodes
# Space O(N)
class Solution:
    def postorder(self, root: "Node") -> List[int]:
        traversal = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    traversal.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    for child in range(len(node.children) - 1, -1, -1):
                        stack.append((node.children[child], False))

        return traversal


# iterative version with same recursion logic -> https://leetcode.com/problems/n-ary-tree-postorder-traversal/discuss/165343/Python-Iterative-Solution-(without-reversing)%3A-same-stack-logic-as-recursive
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        stack, counters, retList = [root], [0], []

        while len(stack) != 0:
            # To English: while the current top of the stack has an unseen child
            while counters[-1] < len(stack[-1].children):
                # Add that child to the top of the stack, with a new corresponding counter to the other stack
                stack.append(stack[-1].children[counters[-1]])
                counters.append(0)
            # If the current top of the stack has reached the end of its children list, then we pop it, it's done
            retList.append(stack.pop().val)
            # need to pop its counter as well
            counters.pop()
            # and increment the counter of the next top of the stack to begin that search
            if len(counters) != 0:
                counters[-1] += 1

        return retList