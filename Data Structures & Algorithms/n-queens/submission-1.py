class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        sublists = []
        for i in range(n):
            nlist = []
            for j in range(n):
                if j == i:
                    nlist.append("Q")
                else:
                    nlist.append(".")
            sublists.append(nlist.copy())
        
        res = []

        def dfs(subsublist, board):
            
            if len(board) == n:
                res.append(board)
                return

            for idx, l in enumerate(subsublist):
                check = False
                x = l.index("Q") - 1
                y = len(board) - 1
                while x >= 0 and y >= 0:
                    if board[y][x] == "Q":
                        check = True
                    x -= 1
                    y -= 1
                x = l.index("Q") + 1
                y = len(board) - 1
                while x < len(l) and y >= 0:
                    if board[y][x] == "Q":
                        check = True
                    x += 1
                    y -= 1
                if check:
                    continue
                else:
                    temp = board.copy()
                    temp.append(l)
                    dfs(subsublist[:idx] + subsublist[idx + 1:], temp)
        
        dfs(sublists, [])

        realres = []

        for board in res:
            nboard = []
            for sublist in board:
                nboard.append("".join(sublist))
            realres.append(nboard.copy())
        
        return realres
                
                        

