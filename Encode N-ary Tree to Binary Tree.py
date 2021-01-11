# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/
# I need to solve it again


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


# BFS
# Time : O(N) for both functions
# Space : O(N) for both functions
class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: "Node") -> TreeNode:
        if not root:
            return None
        root_node = TreeNode(root.val)
        queue = deque([(root_node, root)])
        while queue:
            head, curr = queue.popleft()
            prev_binary_node = None
            head_binary_node = None

            for child in curr.children:
                new_binary_node = TreeNode(child.val)
                if prev_binary_node:
                    prev_binary_node.right = new_binary_node
                else:
                    head_binary_node = new_binary_node
                prev_binary_node = new_binary_node
                queue.append((new_binary_node, child))

            head.left = head_binary_node

        return root_node

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> "Node":
        if not data:
            return None

        root_node = Node(data.val, [])
        queue = deque([(root_node, data)])

        while queue:
            n_ary_node, b_node = queue.popleft()
            child = b_node.left

            while child:
                new_child = Node(child.val, [])
                n_ary_node.children.append(new_child)
                if child.left:
                    queue.append((new_child, child))
                child = child.right

        return root_node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
