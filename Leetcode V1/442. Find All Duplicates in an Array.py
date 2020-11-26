
# my sol
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                res.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
        return res


# check this (better in time a little - not much)
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            n = nums[i]
            if n == 0:
                continue

            nums[i] = -1
            # DFS
            while n != -1:
                if nums[n - 1] == 0:
                    result.append(n)
                    break
                nums[n - 1], n = 0, nums[n - 1]

        return result