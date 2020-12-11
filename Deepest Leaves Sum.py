# https://leetcode.com/problems/deepest-leaves-sum/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# DFS + stack
# time -> O(n)
# space -> O(n)
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        deepest_sum = depth = 0
        stack = [(root, 0)]

        while stack:
            node, node_depth = stack.pop()
            if not node.left and not node.right:
                if node_depth > depth:
                    deepest_sum = node.val
                    depth = node_depth
                elif node_depth == depth:
                    deepest_sum += node.val
            else:
                if node.left:
                    stack.append((node.left, node_depth + 1))

                if node.right:
                    stack.append((node.right, node_depth + 1))
        return deepest_sum


# recursive
# time -> O(n)
# space -> O(H)
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

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


# it can be done in normal BFS

# optimized BFS
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        next_level = deque([root,])

        while next_level:
            # prepare for the next level
            curr_level = next_level
            next_level = deque()

            for node in curr_level:
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

        return sum([node.val for node in curr_level])
