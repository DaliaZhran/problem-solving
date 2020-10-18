class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

    def insertNode(self, key):
        if self.value >= key:
            if self.left:
                self.left.insertNode(key)
            else:
                self.left = Node(key)
                return
        else:
            if self.right:
                self.right.insertNode(key)
            else:
                self.right = Node(key)
                return

    def successor(self, key):
        root = self.right
        while root.left:
            root = root.left
        return root

    def predecessor(self, key):
        root = self.left
        while root.right:
            root = root.right
        return root

    def minValue(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def DeleteNode(self, key):
        if self is None:
            return None
        if key < self.value:
            self.left = self.left.DeleteNode(key)
        elif key > self.value:
            self.right = self.right.DeleteNode(key)
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            temp = self.right.minValue()
            self.value = temp.value
            self.right = self.right.DeleteNode(temp.value)
            return self

    def InOrder(self):
        if self.left:
            self.left.InOrder()
        print(self.value, end=" ")
        if self.right:
            self.right.InOrder()

    # def inorder(root):
    #     return inorder(root.left) + [root.val] + inorder(root.right) if root else []

    def PreOrder(self):
        print(self.value, end=" ")
        if self.left:
            self.left.PreOrder()
        if self.right:
            self.right.PreOrder()

    def PostOrder(self):
        if self.left:
            self.left.PostOrder()
        if self.right:
            self.right.PostOrder()
        print(self.value, end=" ")


tree = Node(4)
tree.insertNode(2)
tree.insertNode(5)
tree.insertNode(7)
tree.insertNode(1)
tree.insertNode(6)
tree.InOrder()
print("")
# tree.DeleteNode(2)
tree.InOrder()
print("")


"""
Notes:
1 - There are many solutions that got high votes using recursive approach, including the ones from the Princeton's Algorithm and Data Structure book. Don't you notice that recursive approach always takes extra space? Why not consider the iterative approach first?
2 - Some solutions swap the values instead of swapping the nodes. In reality, the value of a node could be more complicated than just a single integer, so copying the contents might take much more time than just copying the reference.
3 - As for the case when both children of the node to be deleted are not null, I transplant the successor to replace the node to be deleted, which is a bit harder to implement than just transplant the left subtree of the node to the left child of its successor. The former way is used in many text books too. Why? My guess is that transplanting the successor can keep the height of the tree almost unchanged, while transplanting the whole left subtree could increase the height and thus making the tree more unbalanced.
"""

