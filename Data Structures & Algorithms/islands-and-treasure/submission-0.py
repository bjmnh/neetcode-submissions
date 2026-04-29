class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        search = ((1,0),(-1,0),(0,1),(0,-1))
        def dfs(x,y,steps):
            for dx, dy in search:
                grid[x][y] = steps
                if dx+x >= 0 and dx+x < len(grid) and dy+y >= 0 and dy+y < len(grid[0]) and grid[dx+x][dy+y] > steps:
                    dfs(x+dx, y+dy, steps+1)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    dfs(x,y,0)
        

