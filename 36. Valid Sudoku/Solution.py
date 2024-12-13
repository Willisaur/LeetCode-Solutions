class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxNums = [[0] * 9 for _ in range(9)]
        for i in range(len(board)):
            rowNums = [0] * 9
            colNums = [0] * 9
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    num = int(board[i][j])-1
                    # check row
                    if rowNums[num] == 0:
                        rowNums[num] = 1
                    else:
                        return False
                    # check 3x3 box
                    if boxNums[(i // 3)*3 + j // 3][num] == 0:
                        boxNums[(i // 3)*3 + j // 3][num] = 1
                    else:
                        return False
                if board[j][i] != '.':
                    num = int(board[j][i])-1
                    # check col
                    if colNums[num] == 0:
                        colNums[num] = 1
                    else:
                        return False
        return True