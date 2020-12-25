# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
"""
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS recursive
# time -> O(n)
# space -> O(H) for the recursive stack
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def sumEvenGrandparentDFS(node, p=1, gp=1):
            if not node:
                return 0
            return sumEvenGrandparentDFS(node.left, node.val, p) + sumEvenGrandparentDFS(node.right, node.val, p) + node.val * (1 - gp % 2)

        return sumEvenGrandparentDFS(root)


# DFS recursive -> more intuitive and clear solution
# time -> O(n)
# space -> O(H)
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def sumEvenGrandparentHelper(node, parent, grandparent):
            if not node:
                return 0
            if grandparent and grandparent.val % 2 == 0:
                self.sum += node.val

            sumEvenGrandparentHelper(node.left, node, parent)
            sumEvenGrandparentHelper(node.right, node, parent)

        self.sum = 0
        sumEvenGrandparentHelper(root, None, None)
        return self.sum


# BFS
# time -> O(n)
# space -> O(n)
class Solution(object):
    def sumEvenGrandparent(self, root):
        ans, dq = 0, collections.deque([(root, False)])
        while dq:
            parent, evenGrandParent = dq.popleft()
            evenParent = parent.val % 2 == 0
            for child in parent.left, parent.right:
                if child:
                    dq.append((child, evenParent))
                    ans += child.val if evenGrandParent else 0
        return ans


# A naive approach using nested if conditions solution
# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/discuss/482991/Easy-BFS-solution-in-Java