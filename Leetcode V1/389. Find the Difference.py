
# 1
class Solution(object):
    """
    dictionary
    """
    def findTheDifference(self, s, t):
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        for ch in t:
            if dic.get(ch, 0) == 0:
                return ch
            else:
                dic[ch] -= 1

# 2
class Solution(object):
    """
    difference
    """
    def findTheDifference(self, s, t):
        diff = 0
        for i in range(len(s)):
            diff -= ord(s[i])
            diff += ord(t[i])
        diff += ord(t[-1])
        return chr(diff)

# 3 
class Solution(object):
    """
    xor
    """
    def findTheDifference(self, s, t):
        code = 0
        for ch in s + t:
            code ^= ord(ch)
        return chr(code)

# 3 enhanced -> no concat
class Solution(object):
    """
    xor
    """
    def findTheDifference(self, s, t):
        code = 0
        for ch in s:
            code ^= ord(ch)
        for ch in t:
            code ^= ord(ch)
        return chr(code)