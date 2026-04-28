class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1count = [0] * 26
        s2count = [0] * 26
        matches = 0
        for i in range(len(s1)):
            s1count[ord(s1[i])-ord('a')] += 1
            s2count[ord(s2[i])-ord('a')] += 1
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches += 1
        for i in range(len(s1), len(s2)):
            if matches == 26:
                    return True
            
            if s2count[ord(s2[i])-ord('a')] == s1count[ord(s2[i])-ord('a')]:
                s2count[ord(s2[i])-ord('a')] += 1
                matches -= 1
            else:
                s2count[ord(s2[i])-ord('a')] += 1
                if s2count[ord(s2[i])-ord('a')] == s1count[ord(s2[i])-ord('a')]:
                    matches += 1
            
            if s2count[ord(s2[i - len(s1)])-ord('a')] == s1count[ord(s2[i - len(s1)])-ord('a')]:
                s2count[ord(s2[i - len(s1)])-ord('a')] -= 1
                matches -= 1
            else:
                s2count[ord(s2[i - len(s1)])-ord('a')] -= 1
                if s2count[ord(s2[i - len(s1)])-ord('a')] == s1count[ord(s2[i - len(s1)])-ord('a')]:
                    matches += 1

        return matches == 26


        