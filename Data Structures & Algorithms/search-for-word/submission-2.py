class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(row, col, word_index):
            # if row == rows and cols == cols:
            #     return True
            if word_index == len(word):
                return True
            if row < 0 or row >= rows:
                return False
            if col < 0 or col >= cols:
                return False

            if board[row][col] != word[word_index]:
                return False
            
            # if word_index == len(word)-1:
            #     return False
            tmp = board[row][col]
            board[row][col] = "#"
            found = (
                backtrack(row+1, col, word_index + 1) or
                backtrack(row-1, col, word_index + 1) or
                backtrack(row, col+1, word_index + 1) or
                backtrack(row, col-1, word_index + 1)
            )
            board[row][col] = tmp
            return found

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True
        return False