class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums:
                seq = 1
                while num + seq in nums:
                    seq += 1
                longest = max(seq, longest)
        return longest
        
