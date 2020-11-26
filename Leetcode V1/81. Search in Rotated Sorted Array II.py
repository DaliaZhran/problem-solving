class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums) - 1
        start, end = 0, n
        
        while start <= end:
            mid = (start + end) >> 1
            
            if nums[mid] == target:
                return True
            
            if nums[mid] == nums[start] == nums[end]:
                start += 1
                end -= 1
            
            elif nums[start] <= nums[mid]:  #left part ascending
                # target >= nums[start] to check if target is not the rotated part in right side 
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:                        #right part ascending
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False
            