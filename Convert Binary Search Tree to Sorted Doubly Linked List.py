# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

"""
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# Inorder Traversal
# Time: O(N)
# Space: O(N)
class Solution:
    def treeToDoublyList(self, root: "Node") -> "Node":
        def inorder(node):
            nonlocal first, last
            if node:
                inorder(node.left)
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                inorder(node.right)

        if not root:
            return None

        first, last = None, None
        inorder(root)
        last.right = first
        first.left = last
        return first
