# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS, then get the min diff using loop
# time -> O(n)
# space -> O(n)
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def inOrderTraversal(node):
            return inOrderTraversal(node.left) + [node.val] + inOrderTraversal(node.right) if node else []

        nums = inOrderTraversal(root)
        return min(nums[i + 1] - nums[i] for i in xrange(len(nums) - 1))


# DFS, not required to loop to get min
# time -> O(n)
# space -> O(H) -> recursive Stack
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def inOrderTraversal(node):
            if node:
                inOrderTraversal(node.left)
                self.ans = min(self.ans, node.val - self.prev)
                self.prev = node.val
                inOrderTraversal(node.right)

        self.ans = float("inf")
        self.prev = float("-inf")
        inOrderTraversal(root)
        return self.ans


# different implementation for the prev sol -> no helper function
class Solution(object):
    ans = float("inf")
    prev = float("-inf")

    def minDiffInBST(self, node):
        """
        :type root: TreeNode
        :rtype: int
        """
        if node.left:
            self.minDiffInBST(node.left)
        self.ans = min(self.ans, node.val - self.prev)
        self.prev = node.val
        if node.right:
            self.minDiffInBST(node.right)
        return self.ans

