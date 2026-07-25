class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grids = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            row = set()
            for j in range(9):
                grid_r = i//3
                grid_c = j//3
                if board[i][j] == ".":
                    continue
                if board[i][j] in row:
                    return False
                if board[i][j] in grids[grid_r][grid_c]:
                    return False
                row.add(board[i][j])
                grids[grid_r][grid_c].add(board[i][j])
        for i in range(9):
            col = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in col:
                    return False
                col.add(board[j][i])
        return True
        