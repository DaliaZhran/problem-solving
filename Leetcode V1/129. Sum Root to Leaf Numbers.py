
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        allNums = []
        dfs(root, allNums, [])
        return sum(allNums)

def dfs(node, allNums, num):
    if node == None:
        return
    num.append(str(node.val))

    if node.right == None and node.left == None:
        allNums.append(int("".join(num)))
    else:
        dfs(node.left, allNums, num)
        dfs(node.right, allNums, num)

    del num[-1]

