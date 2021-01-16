# https://leetcode.com/problems/pascals-triangle/

"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""

# Iterative (DP)
# Time : O(numRows^2)
# Space : O(numRows^2)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1] * i for i in range(1, numRows + 1)]
        for row in range(numRows):
            for j in range(1, row):
                result[row][j] = result[row - 1][j - 1] + result[row - 1][j]
        return result


# Nice Idea
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            temp1 = res[-1] + [0]
            temp2 = [0] + res[-1]
            res.append([temp1[i] + temp2[i] for i in range(len(temp1))])
        return res[:numRows]


# Recursive Solution
# Time : O(numRows^2)
# Space : O(numRows^2)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ls = []
        self.generate_recursive(ls, numRows)
        return ls

    def generate_recursive(self, ls, numRows):
        if numRows == 1:
            ls.append([1])
        elif numRows > 1:
            self.generate_recursive(ls, numRows - 1)
            prev_list = ls[numRows - 2]
            this_list = []
            for i in range(len(prev_list)):
                if i == 0:
                    this_list.append(1)
                if i > 0:
                    this_list.append(prev_list[i] + prev_list[i - 1])
                if i == len(prev_list) - 1:
                    this_list.append(1)
            ls.append(this_list)