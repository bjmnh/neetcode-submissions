class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hashmap:
                return [hashmap[val], i]
            
            hashmap[nums[i]] = i
            print(hashmap)
        return []