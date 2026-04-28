class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for idx, num in enumerate(temperatures):
            while stack and num > temperatures[stack[-1]]:
                t = stack.pop()
                result[t] = idx - t
            stack.append(idx)
            print(stack)
        return result
