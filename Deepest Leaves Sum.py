# https://leetcode.com/problems/deepest-leaves-sum/

"""
Given a binary tree, return the sum of values of its deepest leaves.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive
# time -> O(n) since we visit all nodes
# space -> O(H) where H is the height of the tree
class Solution(object):
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def deepestLeavesSumDFS(node, node_depth):
            if not node:
                return
            if not node.left and not node.right:
                if node_depth > self.depth:
                    self.deepest_sum = node.val
                    self.depth = node_depth
                elif node_depth == self.depth:
                    self.deepest_sum += node.val
            deepestLeavesSumDFS(node.left, node_depth + 1)
            deepestLeavesSumDFS(node.right, node_depth + 1)

        self.deepest_sum = self.depth = 0
        deepestLeavesSumDFS(root, 0)
        return self.deepest_sum


# DFS + stack
# time -> O(n)
# space -> up to O(H) to keep the stack, where H is a tree height.
class Solution(object):
    def deepestLeavesSum(self, root: TreeNode) -> int:
        deepest_sum = 0
        deepest_depth = 0
        stack = [(root, 0)]
        # preorder
        while stack:
            node, node_depth = stack.pop()
            if node:
                if not node.left and not node.right:
                    if node_depth > deepest_depth:
                        deepest_sum = node.val
                        deepest_depth = node_depth
                    elif node_depth == deepest_depth:
                        deepest_sum += node.val
                else:
                    stack.append((node.right, node_depth + 1))
                    stack.append((node.left, node_depth + 1))

        return deepest_sum


# it can be done in normal BFS
# time -> O(N) where N is the number of nodes
# space -> up to O(N) since the max number of nodes in a level is N/2 in the case of a complete binary tree
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        deepest_sum = depth = 0
        queue = deque([(root, 0)])

        while queue:
            node, curr_depth = queue.popleft()
            if node.left is None and node.right is None:
                # if this leaf is the deepest one seen so far
                if depth < curr_depth:
                    deepest_sum = node.val  # start new sum
                    depth = curr_depth  # note new depth
                # if there were already leaves at this depth
                elif depth == curr_depth:
                    deepest_sum += node.val  # update existing sum
            else:
                if node.left:
                    queue.append((node.left, curr_depth + 1))
                if node.right:
                    queue.append((node.right, curr_depth + 1))

        return deepest_sum


# optimized BFS
# time -> O(N) where N is the number of nodes
# space -> up to O(N) since the max number of nodes in a level is N/2 in the case of a complete binary tree
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        next_level = [root]
        while next_level:
            curr_level = next_level
            next_level = []
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

        # now curr_level has all last level elements and we need their sum
        return sum([node.val for node in curr_level])


# dfs solution -> good space complexity
# time -> O(N) where N is the number of nodes
# space -> O(H)
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = maxDepth(root)
        return recursiveSum(root, depth)


def recursiveSum(node, d):
    if node == None:
        return 0
    if d == 1:
        return node.val
    return recursiveSum(node.left, d - 1) + recursiveSum(node.right, d - 1)


def maxDepth(node):
    if node == None:
        return 0
    return max(maxDepth(node.left), maxDepth(node.right)) + 1
