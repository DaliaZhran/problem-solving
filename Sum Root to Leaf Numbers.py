# https://leetcode.com/problems/sum-root-to-leaf-numbers/

"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Preorder
# Time : O(N)
# Space : O(H)
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def sumNumbersHelper(node, path, numbers):
            if not node:
                return
            if not node.left and not node.right:
                path.append(node.val)
                numbers.append("".join(map(str, path)))
            sumNumbersHelper(node.left, path + [node.val], numbers)
            sumNumbersHelper(node.right, path + [node.val], numbers)

        numbers = []
        sumNumbersHelper(root, [], numbers)
        numbers = map(int, numbers)
        return sum(numbers)


# Time : O(N)
# Space : O(H)
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def sumNumbersHelper(node, path, numbers):
            if not node:
                return
            if not node.left and not node.right:
                path += str(node.val)
                numbers.append("".join(path))
            sumNumbersHelper(node.left, path + str(node.val), numbers)
            sumNumbersHelper(node.right, path + str(node.val), numbers)

        numbers = []
        sumNumbersHelper(root, "", numbers)
        numbers = map(int, numbers)
        return sum(numbers)


# Recursive Preorder
# calculating number as we go down the tree instead of appending to list
# Time : O(N)
# Space : O(H)
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def sumNumbersHelper(node, path):
            if not node:
                return

            curr_num = node.val + path * 10
            if not node.left and not node.right:
                self.sum += curr_num
            sumNumbersHelper(node.left, curr_num)
            sumNumbersHelper(node.right, curr_num)

        self.sum = 0
        sumNumbersHelper(root, 0)
        return self.sum


# Iterative Preorder
# Time : O(N)
# Space : O(H)
class Solution:
    def sumNumbers(self, root: TreeNode):
        root_to_leaf = 0
        stack = [(root, 0)]

        while stack:
            root, curr_number = stack.pop()
            if root is not None:
                curr_number = curr_number * 10 + root.val
                # if it's a leaf, update root-to-leaf sum
                if root.left is None and root.right is None:
                    root_to_leaf += curr_number
                else:
                    stack.append((root.right, curr_number))
                    stack.append((root.left, curr_number))

        return root_to_leaf


# Accumulate sum
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(node, sum):
            if not node:
                return 0
            if not node.left and not node.right:
                return sum * 10 + node.val
            return helper(node.left, sum * 10 + node.val) + helper(node.right, sum * 10 + node.val)

        return helper(root, 0)


# BFS with queue - changing the nodes values - not recommended though
def sumNumbers2(self, root):
    deque, res = collections.deque(), 0
    if root:
        deque.append(root)
    while deque:
        node = deque.popleft()
        if not node.left and not node.right:
            res += node.val
        if node.left:
            node.left.val += node.val * 10
            deque.append(node.left)
        if node.right:
            node.right.val += node.val * 10
            deque.append(node.right)
    return res


# changing nodes values in DFS too
def sumNumbers(self, root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.val
    val = 0
    if root.left:
        root.left.val += root.val * 10
        val += self.sumNumbers(root.left)
        root.left.val -= root.val * 10
    if root.right:
        root.right.val += root.val * 10
        val += self.sumNumbers(root.right)
        root.right.val -= root.val * 10
    return val