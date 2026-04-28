class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        top = len(numbers) - 1
        bot = 0
        while top > bot:
            check = numbers[top] + numbers[bot]
            if check == target:
                return [bot + 1,top + 1]
            elif check > target:
                top -= 1
            else:
                bot += 1
        return []