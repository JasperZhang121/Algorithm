class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        i = 1
        while k>=0:
            if i not in arr:
                k-=1
            if k==0:
                return i
            i+=1
            
        return -1
            
        
        