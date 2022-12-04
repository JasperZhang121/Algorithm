class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        mapp = collections.defaultdict(list)
        for x in strs:
            temp = sorted(x)
            sort = ''.join(temp)
            mapp[sort].append(x)       
        for x,y in mapp.items():
            res.append(y) 
        return res