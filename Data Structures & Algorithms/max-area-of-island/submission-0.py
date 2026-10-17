class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            count = 1
            stack = [(row, col)]
            visited.add((row, col))
            while stack:
                (row, col) = stack.pop()
                directions = [(1,0), (-1,0),(0,1),(0,-1)]
                for r,c in directions:
                    next_row = row + r
                    next_col = col + c
                    if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or (next_row, next_col) in visited or grid[next_row][next_col] == 0:
                        continue
                    count += 1
                    visited.add((next_row, next_col))
                    stack.append((next_row, next_col))
            return count
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    maxArea = max(maxArea, dfs(row, col))
        return maxArea