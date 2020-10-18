# https://leetcode.com/problems/count-servers-that-communicate/

# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

# Return the number of servers that communicate with any other server.


class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        if not (cols and rows):
            return 0

        res = 0
        rowsServers = [0] * rows
        colsServers = [0] * cols
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    rowsServers[i] += 1
                    colsServers[j] += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (rowsServers[i] > 1 or colsServers[j] > 1):
                    res += 1

        return res


# nice sol -> https://leetcode.com/problems/count-servers-that-communicate/discuss/463287/Python-simple-fast-with-full-explanation
# it saves the positions of the servers to reduce second pass faster
