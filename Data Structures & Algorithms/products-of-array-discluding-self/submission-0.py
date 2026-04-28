class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        backward = [1]
        
        tmp = 1
        p1 = 1

        for i in range(len(nums)-1):
            tmp*= nums[-(i+1)]
            backward.append(tmp)
            print(tmp)
     
        solution = []
        for i in range(len(nums)):

            solution.append(p1*backward[-(i+1)])
            p1*=nums[i]
        
        return solution