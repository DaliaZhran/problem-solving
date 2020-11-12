# https://leetcode.com/problems/sort-an-array/

# merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n > 1:
            mid = n // 2
            left = nums[:mid]
            right = nums[mid:]
            self.sortArray(left)
            self.sortArray(right)

            len_left = len(left)
            len_right = len(right)
            i = j = k = 0
            while i < len_left and j < len_right:
                if right[j] > left[i]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            while i < len_left:
                nums[k] = left[i]
                i += 1
                k += 1
            while j < len_right:
                nums[k] = right[j]
                j += 1
                k += 1
        return nums