class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return n

        s, f = 1, 1
        count = 1
        while s < n and f < n:
            if nums[f] == nums[s-1]:
                if count < 2:
                    count += 1
                    nums[s] = nums[f]
                    s += 1
            else:
                count = 1
                nums[s] = nums[f]
                s += 1
            f += 1

        return s


''' better implementation '''


def removeDuplicates(self, nums):
    n = len(nums)
    k = 2
    if n <= k:
        return n

    s = f = k
    while f < n:
        if nums[s - k] != nums[f]:
            nums[s] = nums[f]
            s += 1
        f += 1
    return s
