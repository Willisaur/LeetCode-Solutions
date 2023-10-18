class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m = # of rows
        # n = # of columns
        matrix = [[0 for x in range(n)] for x in range(m)]

        # return the number of paths from the right square to the end and the below square to the end
        def checkPaths(i, j):
            if i+1 == m and j+1 == n: 
                return 1  # set the finish to 1 path

            accum = 0
            if i < m-1: # don't access a row out of bounds
                accum += matrix[i+1][j]
            if j < n-1: # don't access a column out of bounds
                accum += matrix[i][j+1]
            return accum

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                matrix[i][j] = checkPaths(i, j)

        return matrix[0][0]