# time
# space

# Given a binary tree, return the postorder traversal of its nodes' values.

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [3,2,1]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # iterative
    # we can iterate the tree in preorder but little different: root --> right --> left
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        toVisit = []

        curr = root
        while curr or toVisit:
            while curr:
                toVisit.append(curr)  # append node then append all its rights
                res.insert(0, curr.val)  # append curr node value because it should be at the end, then all rights before it, then lefts
                curr = curr.right

            curr = toVisit.pop()
            # res.append(curr.val) # this is not correct, because postorder is left -> right -> node
            curr = curr.left

        return res


class Solution:
    # a better way for iterative way
    def postorderTraversal(self, root):
        traversal, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    traversal.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return traversal


class Solution:
    # reversed postorder (same idea as preorder) -> node -> right -> left
    def postorderTraversal(self, root):
        traversal, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                # pre-order, right first
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        # reverse result
        return traversal[::-1]


class Solution(object):
    # Recursive
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def postorderTraversalHelper(root, nodes):
            if not root:
                return
            postorderTraversalHelper(root.left, nodes)
            postorderTraversalHelper(root.right, nodes)
            nodes.append(root.val)

        res = []
        postorderTraversalHelper(root, res)
        return res


class Solution(object):
    # recursive again without passing res []
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []

