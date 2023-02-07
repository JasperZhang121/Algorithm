# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        le, ri = 1, n
        
        while le<=ri:
            mid = (le+ri)//2
            if not isBadVersion(mid):
                le = mid+1
            else:
                ri = mid-1
        
        return le
                

