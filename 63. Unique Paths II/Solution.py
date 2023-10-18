class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def calcPaths(i, j):
            if obstacleGrid[i][j] == 1:
                return 0 # is an obstacle = 0 paths
            if i == 0 and j == 0:
                return 1 # is start of grid = 1 path
            
            accum = 0
            if i > 0: # not the first row
                accum += obstacleGrid[i-1][j]
            if j > 0: # not the first column
                accum += obstacleGrid[i][j-1]
            return accum

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                obstacleGrid[i][j] = calcPaths(i, j)

        return obstacleGrid[-1][-1]
