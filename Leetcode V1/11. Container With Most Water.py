
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxProduct = -1

        while left < right:
            product = (right - left) * min(height[left], height[right])
            maxProduct = max(product, maxProduct)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxProduct

# [1,8,6,2,5,4,8,3,7]
