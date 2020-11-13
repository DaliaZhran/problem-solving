# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 2, x//2 
        
        while left <= right:
            mid = left + (right-left)//2
            target = mid * mid
            if target > x:
                right = mid - 1
            elif target < x: 
                left = mid + 1
            else:
                return mid
        
        return right