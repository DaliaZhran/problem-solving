# https://leetcode.com/problems/pascals-triangle-ii/

"""
Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.

Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            line = [1]
            prevLine = self.getRow(rowIndex - 1)
            for i in range(len(prevLine) - 1):
                line.append(prevLine[i] + prevLine[i + 1])
            line.append(1)
            return line


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j - 1]
            row.append(1)
        return row


# Math
# Time : O(rowIndex)
# Space : O(rowIndex) for output
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        row = [1]
        for i in range(1, rowIndex):
            row.append(int(row[-1] * (rowIndex - i + 1) / i))
        row.append(1)
        return row