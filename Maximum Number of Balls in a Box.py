# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/


# Time: O(N)
# Space: O(N)
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = defaultdict(int)
        max_balls = 0
        for num in range(lowLimit, highLimit + 1):
            d_sum = self.digits_sum(num)
            boxes[d_sum] += 1
            max_balls = max(max_balls, boxes[d_sum])

        return max_balls

    def digits_sum(self, num):
        sum = 0
        while num:
            sum += num % 10
            num = num // 10
        return sum