class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False            
        start, end = 0, len(matrix[0])
        row = -1
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                row = i
                break
        if row == -1:
            return False
        
        while start <= end:
            mid = (start + end) >> 1
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False



# better sol
class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    # 8:21
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False