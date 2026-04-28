class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []
        lp, rp = 0, 0
        while rp < len(nums):
            while q and nums[q[-1]] < nums[rp]:
                q.pop()
            q.append(rp)
            while q and q[0] < lp:
                q.popleft()

            if rp - lp + 1 >= k:
                result.append(nums[q[0]])
                lp +=1

            rp +=1
        return result