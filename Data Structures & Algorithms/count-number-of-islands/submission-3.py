class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(row, col):
            if grid[row][col] == "0" or (row,col) in visited:
                return
            visited.add((row, col))

            for r, c in directions:
                next_row = row + r
                next_col = col + c
                if next_row < 0 or next_row >= rows:
                    continue
                if next_col < 0 or next_col >= cols:
                    continue
                if (next_row, next_col) in visited:
                    continue
                dfs(next_row, next_col)
            return
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == "1":
                    count += 1
                    dfs(row, col)
        return count



