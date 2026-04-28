class trie:
    def __init__(self):
        self.children = {}
        self.isend = False
    
class WordDictionary:

    def __init__(self):
        self.root = trie()
        

    def addWord(self, word: str) -> None:
        root = self.root
        for c in word:
            if c not in root.children:
                root.children[c] = trie()
            root = root.children[c]
        root.isend = True     

    def search(self, word: str) -> bool:

        def dfs(x, node) -> bool:
            if x == len(word):
                return node.isend
   
            if word[x] != ".":
                if word[x] not in node.children:
                    return False
                else:
                    return dfs(x+1, node.children[word[x]])
            else:
                for child in node.children:
                    if dfs(x+1, node.children[child]):
                        return True
                return False


        return dfs(0, self.root)    

        
