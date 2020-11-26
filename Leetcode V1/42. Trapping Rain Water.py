class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        answer = 0

        while left < right:
            if height[left] >= height[right]:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    answer += rightMax - height[right]
                right -= 1

            else:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    answer += leftMax - height[left]
                left += 1
        return answer
