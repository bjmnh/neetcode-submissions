class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []
        lp, rp = 0, 0
        while rp < len(nums):
            while q and q[-1][0] < nums[rp]:
                q.pop()
            q.append([nums[rp],rp])
            while q and q[0][1] < lp:
                q.popleft()

            if rp - lp + 1 >= k:
                result.append(q[0][0])
                lp +=1

            rp +=1
        return result