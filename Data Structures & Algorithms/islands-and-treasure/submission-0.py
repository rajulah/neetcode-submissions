from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            (row,col) = queue.popleft()
            for r, c in directions:
                next_row = row + r
                next_col = col + c
                if (next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols):
                    continue
                if grid[next_row][next_col] != 2**31 - 1:
                    continue
                grid[next_row][next_col] = grid[row][col] + 1
                queue.append((next_row, next_col))



