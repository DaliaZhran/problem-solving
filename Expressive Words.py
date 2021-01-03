# https://leetcode.com/problems/expressive-words/


# Time -> O(KN) where K is the max length of a word and N is the number of words
# Space -> O(1)
class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        if not words or S == "":
            return 0
        count = 0
        for w in words:
            count += self.stretchy(S, w)
        return count

    def stretchy(self, S, word):
        s_len = len(S)
        word_len = len(word)
        j = 0  # current index in word
        for i in range(s_len):
            if j < word_len and S[i] == word[j]:
                j += 1
            # check if we are in the 2nd or 3rd occurence in S
            elif S[i - 1 : i + 2] != S[i] * 3 != S[i - 2 : i + 1]:
                return 0

        return j == word_len

    # more intuitive implementation for stretchy function. it depeneds on skipping repeated chars from both words
    def stretchy(self, S, W):
        i, j, i2, j2, n, m = 0, 0, 0, 0, len(S), len(W)
        while i < n and j < m:
            if S[i] != W[j]:
                return False
            while i2 < n and S[i2] == S[i]:
                i2 += 1
            while j2 < m and W[j2] == W[j]:
                j2 += 1
            if i2 - i != j2 - j and i2 - i < max(3, j2 - j):
                return False
            i, j = i2, j2
        return i == n and j == m