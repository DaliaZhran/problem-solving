"""
Space Complexity: O(N*M*C) -> N-number of strings, M-max length of a string, C-size of alphabet
"""

# A class to represent Trie:
class Trie:
    # Constructor
    def __init__(self):

        self.isLeaf = False
        self.children = {}

    # Iterative function to insert a string in Data Structure
    def insert(self, key):
        print("Inserting...", key)
        # start from root node
        curr = self
        # do for each character of the key
        for c in key:
            # go to next node and create one if path doesn't exists
            curr = curr.children.setdefault(c, Trie())

        # mark current node as leaf
        curr.isLeaf = True
        # curr.children["#"] = True  # -> if terminating node is added

    def search(self, key):
        """
        Iterative function to search a key in Trie.
        Returns true if the key is found in the Trie, else it returns false
        :type prefix: str
        :rtype: bool
        """
        print("Searching", key, end=": ")
        curr = self
        # do for each character of the key
        for c in key:
            # go to the next node
            curr = curr.children.get(c)
            # if string is invalid (reached end of path in Trie)
            if curr is None:
                return False

        # return true if current node is a leaf node and we have reached
        # the end of the string
        return curr.isLeaf
        # return curr.children.get("#")  # -> if terminating node is added

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self
        for c in prefix:
            curr = curr.children.get(c)
            if not curr:
                return False
        return True

    # Iterative function to delete a key in Trie. It returns true
    # if the key is deleted from the Trie, else it returns false. Deletion means removing the terminating word flag of the key
    def delete(self, key):
        # if not self:
        #     return False
        curr = self
        for c in key:
            # if string is invalid (reached end of path in Trie)
            if curr is None:
                return False
            curr = curr.children.get(c)

        if not curr:
            return False
        else:
            curr.isLeaf = False
            return True


# Memory efficient implementation of Trie Data Structure in Python
if __name__ == "__main__":

    # construct a node
    head = Trie()

    head.insert("xyz")
    print(head.search("xyz"))
    print(head.delete("xyz"))

