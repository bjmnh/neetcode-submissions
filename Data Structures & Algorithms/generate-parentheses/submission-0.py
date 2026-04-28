class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open, complete, current):
            if complete < n:
                if open > 0:
                    backtrack(open-1, complete + 1, current + ")")
                if open + complete < n:
                    backtrack(open +1, complete, current + "(")
            elif complete == n:
                res.append(current)

        backtrack(0,0,"")
        return res




        