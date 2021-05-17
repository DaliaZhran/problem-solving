# https://leetcode.com/problems/linked-list-in-binary-tree/

"""
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

Example 1:

Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS
# Time O(N * min(L,H))
# Space O(H)
# where N = tree size (number of nodes), H = tree height, L = list length.
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def helper(list_node, tree_node):
            if not list_node:
                return True
            if not tree_node:
                return False
            if list_node.val == tree_node.val:
                return helper(list_node.next, tree_node.left) or helper(list_node.next, tree_node.right)

        if not head:
            return True
        if not root:
            return False
        # cosider the correct list starts on our current path
        return helper(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


# KMP Search -> https://leetcode.com/problems/implement-strstr/
# https://leetcode.com/problems/linked-list-in-binary-tree/discuss/535370/Java-KMP-Search-O(m%2Bn)-Clean-code
