class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        m,n,visited,origin = len(image),len(image[0]), set(), image[sr][sc]
        
        def dfs(x,y):
            if x>=0 and x<m and y>=0 and y<n:
                if (x,y) not in visited and image[x][y]==origin:
                    image[x][y] = color
                    visited.add((x,y))
                    dfs(x-1,y); dfs(x+1,y) ; dfs(x,y-1) ; dfs(x,y+1)
            else:
                return
        
        dfs(sr,sc)
        
        return image
        
        
            
        