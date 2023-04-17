class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxi = max(candies)
        res = []
        
        for x in candies:
            res.append(x+extraCandies>=maxi)
        
        return res