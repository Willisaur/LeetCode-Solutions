class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m = # of rows
        # n = # of columns
        grid = [[0 for x in range(n)] for x in range(m)]

        # return the number of paths from the right square to the end and the below square to the end
        def checkPaths(i, j):
            if i == m or j == n: # out of bounds
                return 0
            if i == m-1 and j == n-1: # at bottom right
                return 1
            if grid[i][j] == 0: # not calculated yet
                grid[i][j] = checkPaths(i+1, j) + checkPaths(i, j+1)
            return grid[i][j]

        return checkPaths(0, 0)