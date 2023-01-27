class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        

        m = len(image)
        n = len(image[0])
        
        visited = [[None for _ in range(n)] for _ in range(m)]
        initialColor = image[sr][sc]
        queue = [(sr,sc)]
        
        while queue:
            sr, sc = queue.pop(0)
            visited[sr][sc] = True
            image[sr][sc] = color
            for dsr, dsc in [(sr+1, sc), (sr-1, sc), (sr, sc+1), (sr, sc-1)]:
                if 0 <= dsr < m and 0 <= dsc < n and not visited[dsr][dsc] and image[dsr][dsc] == initialColor:
                    queue.append((dsr, dsc))
        return image



                
                
                