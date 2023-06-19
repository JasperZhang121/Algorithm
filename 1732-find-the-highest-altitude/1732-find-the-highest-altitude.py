class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi,res = 0, 0

        for x in gain:
            maxi += x
            if maxi > res:
                res = maxi
        
        return res
