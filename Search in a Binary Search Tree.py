# https://leetcode.com/problems/search-in-a-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative
# Time : O(H) where H is between O(N) if the tree is unbalanced and O(log N) if it is balanaced
# Space : O(1)
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if val == root.val:
                break
            elif val < root.val:
                root = root.left
            else:
                root = root.right

        return root


# Recursive
# Time : O(H)
# Space : O(H) -> where O(H) is O(N) in worst case and O(log N) average
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or val == root.val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
