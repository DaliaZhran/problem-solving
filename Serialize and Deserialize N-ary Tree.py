# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# DFS
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """

        def serializeDFS(node):
            if not node:
                return

            serialize_res.append(str(node.val))
            for child in node.children:
                serializeDFS(child)
            serialize_res.append("#")

        serialize_res = []
        serializeDFS(root)
        return ",".join(serialize_res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """

        def deserializeDFS(node):
            if not data_list:
                return

            while data_list[0] != "#":
                val = data_list.pop(0)
                child = Node(int(val), [])
                node.children.append(child)
                deserializeDFS(child)

            data_list.pop(0)

        if not data:
            return None
        data_list = data.split(",")
        root = Node(int(data_list.pop(0)), [])
        deserializeDFS(root)
        return root


# BFS
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        serialize_res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node != "#":
                serialize_res.append(str(node.val))
                for child in node.children:
                    queue.append(child)
                queue.append("#")
            else:
                serialize_res.append("#")

        return ",".join(serialize_res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        data_list = deque(data.split(","))

        root = Node(int(data_list[0]), [])
        queue = deque([root])
        idx = 1

        while queue:
            node = queue.popleft()

            while data_list[idx] != "#":
                val = data_list[idx]
                child = Node(int(val), [])
                node.children.append(child)
                queue.append(child)
                idx += 1

            idx += 1

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

