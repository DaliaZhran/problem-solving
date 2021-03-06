# Not From Leetcode

'''
Given a number ‘n’, implement a method to count how many possible ways there are to express ‘n’ as the sum of 1, 3, or 4.
'''

# Recursive
# Time: O(3^n)
# Space: O(n)
def countWays1(n):
    if n == 0:
        return 1
    if n < 0: 
        return 0
    
    return countWays1(n-1) + countWays1(n-3) + countWays1(n-4)

# Top Down Memoization
# Time: O(n)
# Space: O(n)
def countWays2(n):
    def helper(n):
        if n == 0: return 1
        if n < 0: return 0
        if dp[n] == 0:
            dp[n] = helper(n-1) + helper(n-3) + helper(n-4)
        return dp[n]
    
    dp = [0] * (n+1)
    return helper(n)


# Bottom Up DP
# Time: O(n)
# Space: O(n)
def countWays3(n):
    # we need to carefully check the base cases for these problems
    dp = [1, 1, 1, 2] + [0] * (n-3) 
    for i in range(4, n+1):
        dp[i] = dp[i - 1] + dp[i-3] + dp[i-4]
    return dp[n]


def countWays4(n):
    if n < 3: return 1
    if n == 3: return 2
    
    # p0 -> n - 4
    # p1 -> n - 3
    # p2 -> n - 2
    # p3 -> n - 1
    p0, p1, p2, p3 = 1, 1, 1, 2
    
    for i in range(4, n+1):
        p0, p1, p2, p3 = p1, p2, p3, p0 + p1 + p3
    return p3



for i in range(10):
    print(countWays1(i))
    print(countWays2(i))
    print(countWays3(i))
    print(countWays4(i))
    print('==================')
