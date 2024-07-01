class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        count = 0
        
        for x in arr:
            if count == 3:
                return True
            
            if x%2:
                count +=1
            else:
                count = 0
        
        return count==3
            