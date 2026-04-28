class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            f = list(zip(position, speed))
            f.sort()
            total = 0
            x = len(position) - 1
            while x >= 0:
                timetf = (target - f[x][0])/f[x][1]
                total += 1
                x -= 1
                while x>=0 and (target - f[x][0])/f[x][1] <= timetf:
                    x-= 1
            return total


                