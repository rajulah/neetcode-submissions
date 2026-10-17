class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()
        def dfs(row, col ):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid [row][col] == "0" or (row, col) in visited:
                return
            visited.add((row, col))
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    islands += 1
                    dfs(row, col)
        return islands