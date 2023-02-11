class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        

        if len(s)<len(p):
            return []
        
        pCount = [0]*26
        sCount = [0]*26
        res = []
        
        for char in p:
            pCount[ord(char) - ord('a')] += 1
        
        for i in range(len(s)):
            sCount[ord(s[i]) - ord('a')] += 1 
            
            if i >= len(p):
                sCount[ord(s[i - len(p)]) - ord('a')] -= 1
            
            if pCount == sCount:
                res.append(i-len(p)+1)
        return res