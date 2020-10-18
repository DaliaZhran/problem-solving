# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# DFS
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def serializeDFS(node):
            if not node:
                serialize_res.append("None")
                return
            serialize_res.append(str(node.val))
            serializeDFS(node.left)
            serializeDFS(node.right)

        serialize_res = []
        serializeDFS(root)
        return ",".join(serialize_res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def deserializeDFS(d_List):
            if d_List[0] == "None":
                d_List.pop(0)
                return None
            root = TreeNode(d_List.pop(0))
            root.left = deserializeDFS(d_List)
            root.right = deserializeDFS(d_List)

            return root

        data_list = data.split(",")
        root = deserializeDFS(data_list)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


# BFS
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        serialize_res = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                serialize_res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                serialize_res.append("None")

        return ",".join(serialize_res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        data_list = iter(data.split(","))
        root = TreeNode(next(data_list))
        queue = [root]

        while queue:
            node = queue.pop(0)

            left = next(data_list)
            if left != "None":
                node.left = TreeNode(int(left))
                queue.append(node.left)

            right = next(data_list)
            if right != "None":
                node.right = TreeNode(int(right))
                queue.append(node.right)

        return root

