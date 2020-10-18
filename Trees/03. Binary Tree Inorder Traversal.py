# time
# space

# Given a binary tree, return the inorder traversal of its nodes' values.
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # we can use res directly and remove nodes from parameters
        def inorderTraversalHelper(root, nodes):
            if root is None:
                return
            inorderTraversalHelper(root.left, nodes)
            nodes.append(root.val)
            inorderTraversalHelper(root.right, nodes)

        res = []
        inorderTraversalHelper(root, res)
        return res

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        toVisit = []  # stack

        curr = root
        while curr or toVisit:
            while curr:
                toVisit.append(curr)
                curr = curr.left

            curr = toVisit.pop()
            res.append(curr.val)
            curr = curr.right
        return res
