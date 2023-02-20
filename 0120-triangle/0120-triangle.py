class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        m = len(triangle)
        
        for i in range(m):
            
            if i == 0:
                continue            
            
            else:
                j = 0
                while j <= i:    
                    if j==0:
                        triangle[i][j] += triangle[i-1][j]
                    else:
                        if j <= i-1:
                            triangle[i][j] += min(triangle[i-1][j],triangle[i-1][j-1])
                        else:
                            triangle[i][j] += triangle[i-1][j-1]        
                    j+=1
                    
        return min(triangle[m-1])
            