class Solution {
public:
    int uniquePaths(int m, int n) {
        // m = number of rows
        // n = number of columns
        vector<vector<int>> grid(m, vector<int>(n, 0));
        return calcPaths(0, 0, m, n, grid);
    }
    int calcPaths(int i, int j, int m, int n, vector<vector<int>>& grid){
        if (i == m || j == n){ // out of bounds
            return 0;
        } 
        if (i == m-1 && j == n-1){ // bottom right corner
            return 1; 
        }
        if (grid[i][j] == 0){ // not calculated yet
            grid[i][j] = calcPaths(i+1, j, m, n, grid) + calcPaths(i, j+1, m, n, grid);
        }
        return grid[i][j];  
    }
};