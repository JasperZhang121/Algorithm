class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        lo, hi = 0, len(matrix) * len(matrix[0]) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            r = mid // len(matrix[0])
            c = mid % len(matrix[0])
            if matrix[r][c] == target: return True
            if target > matrix[r][c]: lo = mid + 1
            else: hi = mid - 1
        return False