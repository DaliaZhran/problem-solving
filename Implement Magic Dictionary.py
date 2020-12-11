# https://leetcode.com/problems/implement-magic-dictionary/
"""
Design a data structure that is initialized with a list of different words. Provided a string, you should determine if you can change exactly one character in this string to match any word in the data structure.

Implement the MagicDictionary class:

MagicDictionary() Initializes the object.
void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
bool search(String searchWord) Returns true if you can change exactly one character in searchWord to match any string in the data structure, otherwise returns false.
"""

from collections import defaultdict


class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = defaultdict()

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        for w in dictionary:
            curr = self
            for c in w:
                curr = curr.children.setdefault(c, defaultdict())
            curr["#"] = True

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """

        def search_in_node(word, node):
            for i, ch in enumerate(word):
                if not ch in node:
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


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
