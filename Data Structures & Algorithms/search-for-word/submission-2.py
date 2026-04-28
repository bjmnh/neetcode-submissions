class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        seen = set()

        def getneighbors(x, y):
            neighbors = []
            if x != 0:
                neighbors.append((x-1,y)) 
            if y!= 0:
                neighbors.append((x, y-1))
            if y < len(board[0]) - 1:
                neighbors.append((x, y+1))
            if x < len(board) - 1:
                neighbors.append((x+1,y))
            return neighbors
        
        def check(x,y, w):
            if not w:
                return True
            neighbors = getneighbors(x,y)
            for pair in neighbors:
                if pair in seen:
                    continue
                a,b = pair
                if board[a][b] == w[0]:
                    seen.add((a,b))

                    if check(a,b, w[1:]):
                        return True
                    seen.remove((a,b))
                    

            

        for x, row in enumerate(board):
            for y, entry in enumerate(row):
                if entry == word[0]:
                    seen.add((x,y))
                    if check(x,y, word[1:]):
                        return True
                    seen.remove((x,y))
        return False



