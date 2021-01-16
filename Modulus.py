# Educative Recursion problem

"""
The modulo operation (abbreviated as mod) returns the remainder when a number is divided by another number. The symbol for mod is %.
"""


# Recursive
# Time : O(N//divisor) -> O(N)
# Space : O(N//divisor) -> O(N)
def mod(dividend, divisor):
    if divisor == 0:
        return 0

    if dividend < divisor:
        return dividend

    return mod(dividend - divisor, divisor)


# Iterative
# Time : O(N//4)
# Space : O(1)
def mod(dividend, divisor):
    while dividend >= divisor:
        dividend -= divisor
    return dividend
