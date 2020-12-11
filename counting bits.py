class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num + 1):
            res.append(self.countOnes(i))
        return res

    def countOnes(self, n):
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count


sol = Solution()
print(sol.countBits(5))

