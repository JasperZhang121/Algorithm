class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
   
        triangle = []
        
        for i in range(num_rows):
            row = [None]*(i+1)
            row[0],row[-1]=1,1
            
            for j in range(1,i):
                if i<2:break
                else:
                    row[j]=triangle[i-1][j-1]+triangle[i-1][j]
            triangle.append(row)
        return triangle
       
            