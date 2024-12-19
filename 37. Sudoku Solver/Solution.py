class Solution:
    def backtrack(self, board, cq, rm, cm, bm, i, j):
        # find location of next blank
        # print(f'cq: {cq}')
        nextCell = cq.popleft()

        # find possible digits
        # try another digit in current cell and move to next cell
        boxIndex = i//3*3 + j//3
        for k in range(9):
            if rm[i][k] == 0 and cm[j][k] == 0 and bm[boxIndex][k] == 0:
                # attempt to solve using k
                # print(f'trying {k+1} in {i} {j}')
                rm[i][k] = 1 
                cm[j][k] = 1
                bm[boxIndex][k] = 1
        
                board[i][j] = str(k+1)
                if nextCell == [-1, -1] or self.backtrack(board, cq, rm, cm, bm, nextCell[0], nextCell[1]):
                    return True
                
                # undo work in current cell
                board[i][j] = '.'
                rm[i][k] = 0
                cm[j][k] = 0
                bm[i//3*3 + j//3][k] = 0
        cq.appendleft(nextCell)
        
        # undo work in previous cell
        return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cellQueue = deque([])
        rowMemo = [[0 for _ in range(9)] for _ in range(9)]
        colMemo = [[0 for _ in range(9)] for _ in range(9)]
        boxMemo = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    cellQueue.append([i, j])
                else:
                    cell = int(board[i][j])-1
                    rowMemo[i][cell] = 1
                    colMemo[j][cell] = 1
                    boxMemo[i//3*3 + j//3][cell] = 1
        cellQueue.append([-1, -1])
        
        start = cellQueue.popleft()
        self.backtrack(board, cellQueue, rowMemo, colMemo, boxMemo, start[0], start[1])

