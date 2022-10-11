class Solution:
    def romanToInt(self, s: str) -> int:
        
        mapp = {}
        
        mapp['I'] = 1
        mapp['V'] = 5
        mapp['X'] = 10
        mapp['L'] = 50
        mapp['C'] = 100
        mapp['D'] = 500
        mapp['M'] = 1000
        
        t = 0
        i = 0
        while i<len(s):
            
            if i+1<len(s) and mapp[s[i]]<mapp[s[i+1]]:
                t+=mapp[s[i+1]] - mapp[s[i]]
                i+=2
            else:
                t+=mapp[s[i]]
                i+=1
        return t
        