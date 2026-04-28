class PrefixTree:

    def __init__(self):
        self.trie = {}
        self.pretrie = {}


    def insert(self, word: str) -> None:
        self.trie[word] = True
        for x in range(len(word) + 1):
            self.pretrie[word[:x]] = True

    def search(self, word: str) -> bool:
        if word in self.trie:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.pretrie:
            return True
        return False
        