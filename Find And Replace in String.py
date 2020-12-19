# https://leetcode.com/problems/find-and-replace-in-string/

"""
To some string S, we will perform some replacement operations that replace groups of letters with new ones (not necessarily the same size).

Each replacement operation has 3 parameters: a starting index i, a source word x and a target word y.  The rule is that if x starts at position i in the original string S, then we will replace that occurrence of x with y.  If not, we do nothing.

For example, if we have S = "abcd" and we have some replacement operation i = 2, x = "cd", y = "ffff", then because "cd" starts at position 2 in the original string S, we will replace it with "ffff".

Using another example on S = "abcd", if we have both the replacement operation i = 0, x = "ab", y = "eee", as well as another replacement operation i = 2, x = "ec", y = "ffff", this second operation does nothing because in the original string S[2] = 'c', which doesn't match x[0] = 'e'.

All these operations occur simultaneously.  It's guaranteed that there won't be any overlap in replacement: for example, S = "abc", indexes = [0, 1], sources = ["ab","bc"] is not a valid test case.
"""


# Time -> O(KN) where K is the max length of a source and N is the length of S
# Space -> O(N)
class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        S_list = list(S)
        for index, source, target in zip(indexes, sources, targets):
            if S[index : index + len(source)] == source:
                S_list[index] = target
                for temp in range(index + 1, index + len(source)):
                    S_list[temp] = ""

        return "".join(S_list)


# Time -> Klog(K) for sorting where K is len(indices)
# Space -> O(N)
class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        S_list = list(S)
        for index, source, target in sorted(zip(indexes, sources, targets), reverse=True):
            if S[index : index + len(source)] == source:
                S_list[index : index + len(source)] = target

        return "".join(S_list)


# Time -> O(K) + O(N) where K is len(indexes) and N is len(S)
# Space -> O(N)
class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        valid_indecies = {}
        for i, index in enumerate(indexes):
            if S.startswith(sources[i], index):
                valid_indecies[index] = i

        S_list = []
        i = 0
        while i < len(S):
            if i in valid_indecies:
                Source_index = valid_indecies[i]
                S_list.append(targets[Source_index])
                i += len(sources[Source_index])
            else:
                S_list.append(S[i])
                i += 1
        return "".join(S_list)
