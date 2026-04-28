class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        checkset = set(s1)
        check = sorted(s1)
        for i, letter in enumerate(s2):
            if i > len(s2) - len(s1):
                return False
            if letter in checkset:
                if check == sorted(s2[i:i+len(s1)]):
                    return True
        return False