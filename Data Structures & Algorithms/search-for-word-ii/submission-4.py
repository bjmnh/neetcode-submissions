class Trie:
    def __init__(self):
        self.children = {}
        self.word = None
    def addword(self, word):
        root = self
        for x in range(len(word)):
            if word[x] not in root.children:
                root.children[word[x]] = Trie()
            root = root.children[word[x]]
        root.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        root = Trie()
        for word in words:
            root.addword(word)
        
        

        def dfs(troot, y, x):
            if troot.word:
                res.add(troot.word)
                
            temp = board[y][x]
            board[y][x] = ""
            
            if y > 0 and board[y-1][x] in troot.children:
                dfs(troot.children[board[y-1][x]], y-1,x)
            if y < len(board) - 1 and board[y+1][x] in troot.children:
                dfs(troot.children[board[y+1][x]], y+1,x)
            if x > 0 and board[y][x-1] in troot.children:
                dfs(troot.children[board[y][x-1]], y,x-1)
            if x < len(board[0]) - 1 and board[y][x+1] in troot.children:
                dfs(troot.children[board[y][x+1]], y,x+1)
                
            board[y][x] = temp

        

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] in root.children:
                    dfs(root.children[board[y][x]], y,x)
                      
        return list(res)






        