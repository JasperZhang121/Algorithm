class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        ans = 0
        for i in range(len(grid[0])):
            m1 = -1
            for j in range(len(grid)):
                mx = max(grid[j])
                m1 = max(m1,mx)
                grid[j].remove(mx)
            ans += m1
        return ans
            
        
            