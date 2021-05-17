# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
"""

# Definition for a binary tree node.
# time: O(N)
# space: O(N)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def preorderTraversal(root):
            if not root:
                return []
            return [root] + preorderTraversal(root.left) + preorderTraversal(root.right)

        if not root:
            return root
        res = preorderTraversal(root)[::-1]
        head = node = res.pop()
        while res:
            node.left = None
            node.right = res.pop()
            node = node.right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def preorderTraversal(root):
            if not root:
                return []
            res.append(root)
            preorderTraversal(root.left)
            preorderTraversal(root.right)

        if not root:
            return root
        res = deque()
        preorderTraversal(root)
        node = res.popleft()
        while res:
            node.left = None
            node.right = res.popleft()
            node = node.right
