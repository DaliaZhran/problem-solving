class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insertNode(self, key):
        root = self
        if not root:
            return Node(key)

        queue = []
        while queue:
            root = queue.pop(0)
            if root.left:
                queue.append(root.left)
            else:
                root.left = Node(key)
                return
            if root.right:
                queue.append(root.right)
            else:
                root.right = Node(key)
                return

    def deleteDeepest(self, target_node):
        root = self
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node is target_node:
                node = None
                return
            if node.left:
                if node.left is target_node:
                    node.left = None
                    return
                else:
                    queue.append(node.left)
            if node.right:
                if node.right is target_node:
                    node.right = None
                    return
                else:
                    queue.append(node.right)

    def delete(self, key):
        if not self:
            return self
        if self.left == None and self.right == None:
            if key == self.value:
                return None
            else:
                return self
        queue = [self]
        target_node = None
        while queue:
            node = queue.pop(0)
            if node.value == key:
                target_node = node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if target_node:
            x = node.value
            self.deleteDeepest(node)
            target_node.value = x

        return self

    def inOrderTraversal(self):
        if self.left:
            self.left.inOrderTraversal()
        print(self.value, end=" ")
        if self.right:
            self.right.inOrderTraversal()

    def preOrderTraversal(self):
        print(self.value, end=" ")
        if self.left:
            self.left.inOrderTraversal()
        if self.right:
            self.right.inOrderTraversal()

    def postOrderTraversal(self):
        if self.left:
            self.left.inOrderTraversal()
        if self.right:
            self.right.inOrderTraversal()
        print(self.value, end=" ")

    def levelTraversal(self):
        if not self:
            return
        queue = [self]
        while queue:
            node = queue.pop(0)
            print(node.value, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


tree = Node(3, Node(4, Node(5), Node(6)), Node(2))
tree.inOrderTraversal()
print("")
# tree.delete(3)
tree.inOrderTraversal()
print("")
tree.preOrderTraversal()
print("")
tree.postOrderTraversal()
print("")
tree.levelTraversal()
print("")
