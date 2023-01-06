class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        c = 0
        for x in costs:
            coins-=x
            if coins<0:
                break
            c+=1
        
        return c
            
        
        
            