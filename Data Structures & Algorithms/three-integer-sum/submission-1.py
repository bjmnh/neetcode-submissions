class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) #nlogn
        result = []
        for x in range(len(nums) - 2):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            p1 = x + 1
            p2 = len(nums) - 1
           
            while p1 < p2:

                check = nums[x] + nums[p1] + nums[p2]
                if check == 0:
                    result.append([nums[x],nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    while p1 < p2 and nums[p1] == nums[p1-1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2+1]:
                        p2 -= 1
                elif check > 0:
                    p2 -= 1
                else:
                    p1 += 1
        return result