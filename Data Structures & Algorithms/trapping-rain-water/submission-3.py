class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = height[0]
        rightmax = height[len(height)-1]
        p1 = 0
        p2 = len(height) - 1
        total = 0
        while p1 < p2:
            if leftmax > rightmax:
                p2 -= 1
                rightmax = max(rightmax, height[p2])
                total += rightmax - height[p2]
            else:
                p1 += 1
                leftmax = max(leftmax, height[p1])
                total += leftmax - height[p1]

        return total