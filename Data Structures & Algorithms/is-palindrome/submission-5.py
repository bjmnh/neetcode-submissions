class Solution:
    def isPalindrome(self, s: str) -> bool:
        pnome = [char.lower() for char in s if char.isalnum()]
        return pnome == pnome[::-1]