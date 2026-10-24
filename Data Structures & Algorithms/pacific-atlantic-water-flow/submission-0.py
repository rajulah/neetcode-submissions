class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # input -> heights
        # heights[r][c] -> height above sea level
        # water flows -> 4 directions if neighbor height <= this cell's height
        # water flows -> from edge cells to ocean
        # find all cells, where water can flow to both pacific and atlantic
       #1.  we will do dfs from r = 0 or c = 0 cells (pacific) and note down all cells we can reach from there
    # 2. repeat dfs on all cells with r = len(rows)-1 or c = len(cols) - 1 and note down
    # all cells that can be reached
    # 3. get the intersection of the set of 1 and 2 and return it
        pacific_set = set()
        atlantic_set = set()
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        reachable = set()
        def dfs(row, col, reachable):
            reachable.add((row, col))
            for r,c in directions:
                next_row = row + r
                next_col = col + c
                if next_row < 0 or next_row >= rows:
                    continue
                if next_col < 0 or next_col >= cols:
                    continue
                if (next_row, next_col) in reachable:
                    continue
                if heights[next_row][next_col] < heights[row][col]:
                    continue
                dfs(next_row, next_col, reachable)
            return
        
        # PACIFIC DFS
        for c in range(cols):
            dfs(0, c, pacific_set)
        for r in range(rows):
            dfs(r, 0, pacific_set)
        
        #ATLANTIC DFS
        for c in range(cols):
            dfs(rows-1, c, atlantic_set)
        for r in range(rows):
            dfs(r, cols-1, atlantic_set)

        result = pacific_set & atlantic_set
        result = [list(i) for i in result]
        return result
            
