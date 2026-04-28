class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #segment board into three parts
        #rows (already done)
        #columns (inverse [y][x] so we can access columns? how to do in python)
        #quadrants ([floory/3][floorx/3])
        #convert these segments into sets and compare length to list
        #if any are smaller, return false
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        quads = collections.defaultdict(set)
 
        for y in range(9):
            for x in range(9):
                if board[y][x] != ".":
                    if board[y][x] in rows[y]: return False
                    else: rows[y].add(board[y][x])
                    if board[y][x] in cols[x]: return False
                    else: cols[x].add(board[y][x])
                    if board[y][x] in quads[(y//3,x//3)]: return False
                    else: quads[(y//3,x//3)].add(board[y][x])
                
        return True