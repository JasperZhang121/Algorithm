class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        return sum(1 for row in grid for num in row if num < 0)