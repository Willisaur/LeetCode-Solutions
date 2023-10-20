class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m = number of rows
        # n = number of columns

        grid = [[0 for x in range(n)] for x in range(m)] # dual list comprehension
        """
        for a 3x4 (m x n):
        [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
        """

        # return the number of unique paths in the right cell and below cell
        def checkPaths(i, j):
            # base case
            # if at the start/top left corner, return 1
            if j == 0 and i == 0:
                return 1
            
            accum = 0 # number of unique paths to this cell
            # out-of-bounds checking
            if i < m: # columns (going too far down)
                accum += grid[i-1][j]
            if j < n: # rows (going too far right)
                accum += grid[i][j-1]
            return accum
        
        for i in range(m): # rows (going down)
            for j in range(n): # columns (going right)
                grid[i][j] = checkPaths(i, j)

        print(grid)
        return grid[-1][-1] # print the finish cell value