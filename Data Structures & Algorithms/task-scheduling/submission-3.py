class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        most = max(freq)
        kmost = 0
        for num in freq:
            if num == most:
                kmost += 1
        
        return max(len(tasks), (most - 1) * (n + 1) + kmost)
