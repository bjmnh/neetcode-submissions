class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        f = sorted(zip(position, speed), reverse = True)
        fspeed = 0
        result = 0
        for p, s in f:
            cspeed = (target-p)/s
            if cspeed > fspeed:
                result += 1
                fspeed = cspeed
        return result
