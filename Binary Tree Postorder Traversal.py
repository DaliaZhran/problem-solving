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

# iterative
# # we can iterate the tree in preorder but little different: root --> right --> left
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = deque()
        stack = deque()
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                res.appendleft(curr.val)  # append curr node value because it should be at the end, then all rights before it, then lefts
                curr = curr.right

            curr = stack.pop()
            curr = curr.left
        return res


# A more intuitive iterative solution
class Solution:
    def postorderTraversal(self, root):
        traversal = []
        stack = [(root, False)]
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


# Reversed postorder (same idea as preorder) -> node -> right -> left
class Solution:
    def postorderTraversal(self, root):
        traversal, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                # in pre-order, right is added to stack first
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        # reverse result
        return traversal[::-1]


# Recursive
class Solution(object):
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


# This solution does not work because postorderTraversal gets called multiple times and nodes does not get re-instantiated
class Solution:
    nodes = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.nodes.append(root.val)
        return self.nodes


# Recursive again without passing res []
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
