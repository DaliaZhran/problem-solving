from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Iterative BFS
# Time complexity: O(N) since one has to visit each node.
# Space complexity: O(D) to keep the queues, where D is a tree diameter. Let's use the last level to estimate the queue size.
# This level could contain up to N/2 tree nodes in the case of complete binary tree.
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            for i in range(levelSize):
                el = queue.popleft()
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            result.append(el.val)

        return result


# DFS
# Time complexity: O(N) since one has to visit each node.
# Space complexity: O(H) to keep the recursion stack, where H is a tree height. The worst-case situation is a skewed tree, when H = N
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def helper(node, answer, level):
            if not node:
                return None
            if level == len(answer):
                answer.append(node.val)

            helper(node.right, answer, level + 1)  # we start going through all right children first
            helper(node.left, answer, level + 1)

        answer = []
        helper(root, answer, 0)
        return answer


# Good Article -> https://leetcode.com/problems/binary-tree-right-side-view/solution/