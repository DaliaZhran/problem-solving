# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS
# time -> O(N log N) -> O(N) for BFS and O(N log N) for sorting keys
# space -> O(N)
# Note: we can just use indexing in the queue instead of poping left -> faster
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return root
        queue = deque([(root,0)])
        res_map = defaultdict(list) # avoids the key error if not exist and create a default key 
        
        while queue:
            node, col = queue.popleft()
            if node:
            	res_map[col].append(node.val)
                queue.append((node.left, col - 1))   
                queue.append((node.right, col + 1))
        
        res = []
        for column in sorted (res_map.keys()):
            res.append(res_map[column])
        return res



# BFS
# time -> O(N) -> O(N) for BFS and no sorting
# space -> O(N)
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return root
        queue = deque([(root,0)])
        res_map = defaultdict(list) 
        min_col, max_col = 0, 0
        while queue:
            node, col = queue.popleft()
            if node:
                min_col, max_col = min(col,min_col), max(col, max_col)
                res_map[col].append(node.val)
                queue.append((node.left, col - 1))   
                queue.append((node.right, col + 1))
        
        res = []
        for column in range(min_col, max_col +1):
            res.append(res_map[column])
        return res




# DFS
# time -> O(W * H log H) -> due to sorting each column -> W is the # of cols and H is the height
# space -> O(N)
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def DFS(node, row, column):
            if node is not None:
                nonlocal min_column, max_column
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        DFS(root, 0, 0)

        # order by column and sort by row
        ret = []
        for col in range(min_column, max_column + 1):
            columnTable[col].sort(key=lambda x:x[0])
            colVals = [val for row, val in columnTable[col]]
            ret.append(colVals)

        return ret