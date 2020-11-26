class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return self.subarraysWithAtMostKDistinct(A, K) - self.subarraysWithAtMostKDistinct(A, K-1)

    def subarraysWithAtMostKDistinct(self, A, K):
        substringLetters = {}
        start, end = 0, 0
        count = 0

        while end < len(A):
            right = A[end]
            end += 1
            if right not in substringLetters:
                substringLetters[right] = 0
            substringLetters[right] += 1

            # if len(substringLetters) == K:
            #     count += 1

            while start < end and len(substringLetters) > K:
                left = A[start]
                start += 1
                if substringLetters[left] == 1:
                    del substringLetters[left]
                else:
                    substringLetters[left] -= 1
            count += end - start
        return count
