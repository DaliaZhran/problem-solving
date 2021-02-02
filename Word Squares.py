# https://leetcode.com/problems/word-squares/


# Backtracking
# Time: O(N^2 * 26^L) -> L is len(words[0]). N is the len(words)
# One problem here is -> the use of hashmap didnt improve the time complexity much as in the worst case it is still O(N)
# we can improve this by recording all prefixes and the corresponding words in the hashmap

# Space: O(N^2 * L)
# - L for recursion stack as height of tree would be length of a word
# - Each time, we get candidates in O(N)
# - we repeat the last steps for N times
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def solve(step, curr_path):
            if step == N:
                res.append(curr_path[:])
                return

            for candidate in search("".join(word[step] for word in curr_path)):
                curr_path.append(candidate)
                solve(step + 1, curr_path)
                curr_path.pop()

        def search(target_initials):
            candidates = []
            length = len(target_initials)
            for word in mp[target_initials[0]]:
                if word[:length] == target_initials:
                    candidates.append(word)
            return candidates

        res = []
        N = len(words[0])
        mp = defaultdict(list)
        for word in words:
            mp[word[0]].append(word)

        for word in words:
            solve(1, [word])
        return res


# Backtracking with prefix hashmap
# Record all prefixes and the corresponding words in the hashmap
# Time: O(N * 26^L)
# Space: O(N*L)
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def solve(step, curr_path):
            if step == N:
                res.append(curr_path[:])
                return

            for candidate in search("".join(word[step] for word in curr_path)):
                curr_path.append(candidate)
                solve(step + 1, curr_path)
                curr_path.pop()

        def search(prefix):
            return mp[prefix]

        res = []
        N = len(words[0])
        mp = defaultdict(set)
        for word in words:
            for i in range(1, N):
                mp[word[:i]].add(word)

        for word in words:
            solve(1, [word])
        return res


# Backtracking with Trie
# Time: O(N * 26^L * L)
# Space: O(N*L)
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:

        self.words = words
        self.N = len(words[0])
        self.buildTrie(self.words)

        results = []
        word_squares = []
        for word in words:
            word_squares = [word]
            self.backtracking(1, word_squares, results)
        return results

    def buildTrie(self, words):
        self.trie = {}

        for wordIndex, word in enumerate(words):
            node = self.trie
            for char in word:
                if char in node:
                    node = node[char]
                else:
                    newNode = {}
                    newNode["#"] = []
                    node[char] = newNode
                    node = newNode
                node["#"].append(wordIndex)

    def backtracking(self, step, word_squares, results):
        if step == self.N:
            results.append(word_squares[:])
            return

        prefix = "".join([word[step] for word in word_squares])
        for candidate in self.getWordsWithPrefix(prefix):
            word_squares.append(candidate)
            self.backtracking(step + 1, word_squares, results)
            word_squares.pop()

    def getWordsWithPrefix(self, prefix):
        node = self.trie
        for char in prefix:
            if char not in node:
                return []
            node = node[char]
        return [self.words[wordIndex] for wordIndex in node["#"]]
