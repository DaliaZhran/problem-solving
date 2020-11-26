# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        allPaths = []
        recursivePathSum(root, sum, [], allPaths)
        return allPaths


def recursivePathSum(currentNode, sum, currentPath, allPaths):
    if currentNode == None:
        return

    currentPath.append(currentNode.val)

    if (
        currentNode.val == sum
        and currentNode.right == None
        and currentNode.left == None
    ):
        allPaths.append(list(currentPath))
    else:
        recursivePathSum(currentNode.left, sum - currentNode.val, currentPath, allPaths)
        recursivePathSum(
            currentNode.right, sum - currentNode.val, currentPath, allPaths
        )

    del currentPath[-1]
