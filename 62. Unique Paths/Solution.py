class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m = number of rows
        # n = number of columns

        grid = [[0 for x in range(n)] for x in range(m)]

        # return the number of paths from the right cell to the end and below cell to the end
        def checkPaths(i, j):
            # base case
            # if at the bottom right corner, return 1
            if i + 1 == m and j + 1 == n:
                return 1
            
            accum = 0 # number of paths
            # don't go out of bounds
            if i < m-1: # columns
                accum += grid[i+1][j]
            if j < n-1: # rows
                accum += grid[i][j+1]
            return accum
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                grid[i][j] = checkPaths(i, j)

        return grid[0][0]