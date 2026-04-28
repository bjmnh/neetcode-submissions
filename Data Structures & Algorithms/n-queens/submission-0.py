class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        #Need some way to generate sublists [0,0,0,1]
        #Of length n with 1 in every position

        sublists = []
        for i in range(n):
            nlist = []
            for j in range(n):
                if j == i:
                    nlist.append(1)
                else:
                    nlist.append(0)
            sublists.append(nlist.copy())
        
        #Now we could brute force by generating every single combination
        # of sublists and then verifying if they meet requirements

        #Or a smarter way would be to only construct plausible groups
        #by implementing checks during construction (ie check the diagonals)
        # But I cant come up with a way to check which first rows will be
        # viable, so I would need a way to prune afterwards anyways...
        # Maybe I could prune them as we go, if at layer 3 there are any
        # that still only have 2 layers (bc rules stopped them from adding)
        # then we will just prune it. I think that's the answer

        res = []

        def dfs(subsublist, board):
            
            if len(board) == n:
                res.append(board)
                return

            for idx, l in enumerate(subsublist):
                check = False
                x = l.index(1) - 1
                y = len(board) - 1
                while x >= 0 and y >= 0:
                    if board[y][x] == 1:
                        check = True
                    x -= 1
                    y -= 1
                x = l.index(1) + 1
                y = len(board) - 1
                while x < len(l) and y >= 0:
                    if board[y][x] == 1:
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
            b = []
            for sublist in board:
                strconvert = ""
                for num in sublist:
                    if num:
                        strconvert += "Q"
                    else:
                        strconvert += "."
                b.append(strconvert)
            realres.append(b)
                    

        print(res)
        print(realres)

        return realres
                
                        

