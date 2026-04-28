class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(x,y):
            if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and grid[x][y] == '1':
                grid[x][y] = '0'
                search = ((-1,0), (1,0), (0,-1),(0,1))
                for a, b in search:
                    dfs(x + a, y + b)

        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):

                if grid[x][y] == "1":
                    dfs(x, y)
                    res += 1
        return res 

       
            
