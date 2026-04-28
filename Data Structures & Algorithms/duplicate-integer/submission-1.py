class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = []
        for num in nums:
            if num in a:
                return True
            a.append(num)
        return False