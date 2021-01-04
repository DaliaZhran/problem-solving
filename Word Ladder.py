# https://leetcode.com/problems/word-ladder/

"""
Given two words beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Return 0 if there is no such transformation sequence.

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.
"""

from collections import defaultdict

# Time Complexity: O(MxN^2)
# Space Complexity: O(MxN)
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + c + word[i + 1 :]
                    if next_word in wordList:  # in keyword time is O(N)
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0


# BFS
# Time Complexity: O(M^2xN)
# Space Complexity: O(M^2xN)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0

        word_length = len(beginWord)
        generic_dict = defaultdict(list)
        for word in wordList:
            for i in range(word_length):
                generic_dict[word[:i] + "*" + word[i + 1 :]].append(word)

        print(generic_dict)
        queue = deque([(beginWord, 1)])
        visited = set(beginWord)
        while queue:
            current_word, level = queue.popleft()
            for i in range(word_length):
                intermediate_word = current_word[:i] + "*" + current_word[i + 1 :]

                for word in generic_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))

                generic_dict[intermediate_word] = []

        return 0


# Optimization: We can definitely reduce the space complexity of this algorithm by storing the indices corresponding to each word instead of storing the word itself.


# Bidirectional Breadth First Search
# Time Complexity: O(M^2xN)
# Space Complexity: O(M^2xN)
class Solution(object):
    def __init__(self):
        self.length = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.popleft()
        for i in range(self.length):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i + 1 :]

            # Next states are all the words which share the same intermediate state.
            for word in self.all_combo_dict[intermediate_word]:
                # If the intermediate state/word has already been visited from the
                # other parallel traversal this means we have found the answer.
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    # Save the level as the value of the dictionary, to save number of hops.
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)

        # Queues for birdirectional BFS
        queue_begin = collections.deque([(beginWord, 1)])  # BFS starting from beginWord
        queue_end = collections.deque([(endWord, 1)])  # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None

        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:

            # One hop from begin word
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            # One hop from end word
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0