from collections import defaultdict


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = defaultdict()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        curr = self
        for c in word:
            curr = curr.children.setdefault(c, WordDictionary())
        curr.children["#"] = True

    # Time complexity: O(M) for the "well-defined" words without dots, where M is the key length, and N is a number of keys, and O(M⋅N) for the "undefined" words.
    # Space complexity: O(1) for the search of "well-defined" words without dots, and up to O(M) for the "undefined" words, to keep the recursion stack.
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        def search_in_node(word, node):
            for i, ch in enumerate(word):
                if not ch in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == ".":
                        for x in node:
                            if x != "#" and search_in_node(word[i + 1 :], node[x].children):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node[ch].children
            return "#" in node

        return search_in_node(word, self.children)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


"""
NICE SOLUTION USING Dictionaries - No DFS & Intuitive
"""


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(set)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        self.d[len(word)].add(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        m = len(word)
        for dict_word in self.d[m]:
            i = 0
            while i < m and (dict_word[i] == word[i] or word[i] == "."):
                i += 1
            if i == m:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
