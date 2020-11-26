class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0 or len(words[0]) == 0:
            return []

        wordLen = len(words[0])
        wordsCount = len(words)
        wordFreq = {}
        indecies = []

        for word in words:
            if word not in wordFreq:
                wordFreq[word] = 0
            wordFreq[word] += 1

        for i in range(len(s) - wordLen * wordsCount + 1):
            wordsSeen = {}
            for j in range(0, wordsCount):
                start = i + j * wordLen
                word = s[start: start + wordLen]

                if word not in wordFreq:
                    break

                if word not in wordsSeen:
                    wordsSeen[word] = 0
                wordsSeen[word] += 1

                if wordsSeen[word] > wordFreq[word]:
                    break

                if j+1 == wordsCount:
                    indecies.append(i)
        return indecies
