from collections import deque
class Solution:
    # BFS iterative
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        def bfs(row, col):
            queue = deque([(row, col)])
            visited.add((row, col))
            while queue:
                (row, col) = queue.popleft()

                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for r, c in directions:
                    new_row = row + r
                    new_col = col + c
                    if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or grid[new_row][new_col] == "0" or (new_row, new_col) in visited:
                        continue
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    islands += 1
                    bfs(row, col)
        return islands