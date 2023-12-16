class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        def searchLand(i, j):
            visited[i][j] = 1
            if i-1 >= 0: # check upper bound
                if visited[i-1][j]==0 and grid[i-1][j]=="1": # land and unvisited
                    searchLand(i-1, j) # go up
            if j-1 >= 0: # check left bound
                if visited[i][j-1]==0 and grid[i][j-1]=="1": # land and unvisited
                    searchLand(i, j-1) # go left
            if i+1 <= len(grid)-1: # check lower bound
                if visited[i+1][j]==0 and grid[i+1][j]=="1": # land and unvisited
                    searchLand(i+1, j) # go down
            if j+1 <= len(grid[0])-1: # check right bound
                if visited[i][j+1]==0 and grid[i][j+1]=="1": # land and unvisited
                    searchLand(i, j+1) # go right

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 0 and grid[i][j] == "1": # first time reaching this island
                    island_count += 1
                    searchLand(i, j)
        
        return island_count
    