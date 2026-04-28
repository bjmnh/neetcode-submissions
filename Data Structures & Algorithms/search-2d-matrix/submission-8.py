class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix[0])
        columns = len(matrix)

        lp = 0
        rp = rows*columns - 1
        while lp <= rp:
            mid = (rp + lp)//2
            if matrix[mid//rows][mid%rows] == target:
                return True
            elif matrix[mid//rows][mid%rows] > target:
                rp = mid - 1
            else:
                lp = mid + 1
        return False