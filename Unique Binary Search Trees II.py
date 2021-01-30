# https://leetcode.com/problems/unique-binary-search-trees-ii/

"""
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTreesRecursive(s, e):
            if s > e:
                return [None]

            all_trees = []
            for i in range(s, e + 1):
                left_subtree = generateTreesRecursive(s, i - 1)
                right_subtree = generateTreesRecursive(i + 1, e)

                for l in left_subtree:
                    for r in right_subtree:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)

            return all_trees

        return generateTreesRecursive(1, n)


"""
Here is an easy way to explain the time complexity.
If you have a tree with branching of b and max depth of m, the total number of nodes in this tree in worst case: 1 + b + b^2 + ... + b^(m-1), which is a sum of geometric sequence: (b^m-1)/(b-1). So you can say that time complexity is O(b^m). For the example above it will be O(n*2^n). It is not exact as a Catalan number but I think it is enough in an interview.
"""
