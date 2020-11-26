class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False            
        # start, end = 0, len(matrix[0])
        for row in range(len(matrix)):
            if matrix[row][-1] >= target:            
                start, end = 0, len(matrix[0])
                
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
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False            
        m = len(matrix)
        n = len(matrix[0])
        
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
        return False