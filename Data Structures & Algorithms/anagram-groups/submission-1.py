class Solution:

    def makeTuple(self, word: str) -> tuple:
        count = [0] * 26
        for letter in word:
            count[ord(letter) - ord('a')] += 1
        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dlist = {}
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            
            if tuple(count) not in dlist:
                dlist[tuple(count)] = []
            dlist[tuple(count)].append(word)
        return list(dlist.values())
        

            
