class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        clen = 0
        maxlen = 0
        check = ((1,0),(-1,0),(0,1),(0,-1))
        def dfs(x,y):
            nonlocal clen, maxlen
            if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and grid[x][y] == 1:
                grid[x][y] = 0
                clen += 1
                maxlen = max(maxlen, clen)
                for dx, dy in check:
                    dfs(x + dx, y + dy)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    clen = 0
                    dfs(x,y)
        return maxlen
                