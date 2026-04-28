class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) ==0:
            return []
        res = []
        cur = []

        def dfs(idx):

            if idx >= len(digits):
                res.append("".join(cur))
                return

            match int(digits[idx]):

                case 2:
                    cur.append( "a")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "b")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "c")
                    dfs(idx+1)
                    cur.pop()
                case 3:
                    cur.append( "d")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "e")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "f")
                    dfs(idx+1)
                    cur.pop()
                case 4:
                    cur.append( "g")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "h")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "i")
                    dfs(idx+1)
                    cur.pop()
                case 5:
                    cur.append( "j")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "k")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "l")
                    dfs(idx+1)
                    cur.pop()
                case 6:
                    cur.append( "m")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "n")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "o")
                    dfs(idx+1)
                    cur.pop()
                case 7:
                    cur.append( "p")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "q")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "r")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "s")
                    dfs(idx+1)
                    cur.pop()
                case 8:
                    cur.append( "t")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "u")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "v")
                    dfs(idx+1)
                    cur.pop()
                case 9:
                    cur.append( "w")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "x")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "y")
                    dfs(idx+1)
                    cur.pop()
                    cur.append( "z")
                    dfs(idx+1)
                    cur.pop()



        dfs(0)
        return res