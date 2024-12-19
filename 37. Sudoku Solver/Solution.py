class Solution:
    def backtrack(self, board, cq, rm, cm, bm, i, j):
        # find location of next blank
        # print(f'cq: {cq}')
        nextCell = cq.popleft()

        # find possible digits
        # try another digit in current cell and move to next cell
        boxIndex = i//3*3 + j//3
        for k in range(9):
            if k not in rm[i] and k not in cm[j] and k not in bm[boxIndex]:
                # attempt to solve using k
                # print(f'trying {k+1} in {i} {j}')
                rm[i].add(k)
                cm[j].add(k)
                bm[boxIndex].add(k)
        
                board[i][j] = str(k+1)
                if nextCell == [-1, -1] or self.backtrack(board, cq, rm, cm, bm, nextCell[0], nextCell[1]):
                    return True
                
                # undo work in current cell
                board[i][j] = '.'
                rm[i].remove(k)
                cm[j].remove(k)
                bm[boxIndex].remove(k)
        cq.appendleft(nextCell)
        
        # undo work in previous cell
        return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        cellQueue = deque([])
        rowMemo = [set() for _ in range(9)]
        colMemo = [set() for _ in range(9)]
        boxMemo = [set() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    cellQueue.append([i, j])
                else:
                    cell = int(board[i][j])-1
                    rowMemo[i].add(cell)
                    colMemo[j].add(cell)
                    boxMemo[i//3*3 + j//3].add(cell)
        cellQueue.append([-1, -1])
        
        start = cellQueue.popleft()
        self.backtrack(board, cellQueue, rowMemo, colMemo, boxMemo, start[0], start[1])

