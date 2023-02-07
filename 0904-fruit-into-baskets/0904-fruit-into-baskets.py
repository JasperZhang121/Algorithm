class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        ma,l,res,n,total = collections.defaultdict(int),0,0,len(fruits),0
        
        for r in range(n):
            ma[fruits[r]]+=1
            total+=1
            
            while len(ma)>2:
                f = fruits[l]
                ma[f]-=1
                total-=1
                l+=1
                
                if not ma[f]:
                    ma.pop(f)
            
            res = max (res,total)
        
        return res 
            
                