class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        def dfs(row, col):
            stack = [(row, col)]
            visited.add((row, col))
            while stack:
                row, col = stack.pop()

                # if grid[row][col] == "0" or (row,col) in visited:
                #     continue
                
                # visited.add((row, col))
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for direction in directions:
                    next_row = row + direction[0]
                    next_col = col + direction[1]
                    if next_row < 0 or next_row >= len(grid) or next_col < 0 or next_col >= len(grid[0]) or (next_row, next_col) in visited or grid[next_row][next_col] == "0":
                        continue
                    visited.add((next_row, next_col))
                    stack.append((next_row, next_col))
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != "0" and (row, col) not in visited:
                    print(row, col)
                    islands += 1
                    dfs(row, col)
        return islands






