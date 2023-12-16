class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        area = 0

        def searchLand(i, j):
            visited[i][j] = 1
            area = 0
            if i-1 >= 0: # check upper bound
                if visited[i-1][j]==0 and grid[i-1][j]: # land and unvisited
                    area += 1 + searchLand(i-1, j) # go up
            if j-1 >= 0: # check left bound
                if visited[i][j-1]==0 and grid[i][j-1]: # land and unvisited
                    area += 1 + searchLand(i, j-1) # go left
            if i+1 <= len(grid)-1: # check lower bound
                if visited[i+1][j]==0 and grid[i+1][j]: # land and unvisited
                    area += 1 + searchLand(i+1, j) # go down
            if j+1 <= len(grid[0])-1: # check right bound
                if visited[i][j+1]==0 and grid[i][j+1]: # land and unvisited
                    area += 1 + searchLand(i, j+1) # go right
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 0 and grid[i][j]: # first time reaching this island
                    area = max(area, 1+searchLand(i, j))
        
        return area
                    

