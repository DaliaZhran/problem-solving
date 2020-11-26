class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        currChars = {}
        maxx = 0
        while r < len(s):
            if s[r] in currChars:
                l = max(currChars[s[r]], l)
            currChars[s[r]] = r + 1
            maxx = max(r - l + 1, maxx)
            r += 1
        return maxx