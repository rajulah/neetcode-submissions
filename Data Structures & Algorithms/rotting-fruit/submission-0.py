from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                (row, col) = queue.popleft()
                for r,c in directions:
                    next_row = row + r
                    next_col = col + c
                    if next_row < 0 or next_row >= rows:
                        continue
                    if next_col < 0 or next_col >= cols:
                        continue
                    # print(next_row, next_col, grid[next_row][next_col])

                    if grid[next_row][next_col] == 0 or grid[next_row][next_col] == 2:
                        continue
                    # print("before - ",next_row, next_col, grid[next_row][next_col])
                    grid[next_row][next_col] = 2
                    # print("after - ",next_row, next_col, grid[next_row][next_col])

                    queue.append((next_row, next_col))
                    fresh -= 1
            minutes += 1
            # print(minutes, grid)

        return minutes if fresh == 0 else -1
            
