class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        wordSet,res = set(words),[] 
        
        def dfs(word):
            for i in range(1,len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if ((prefix in wordSet and suffix in wordSet) or (prefix in wordSet and dfs(suffix))):
                    return True
                
        for x in words:
            if dfs(x): res.append(x)
        
        return res
            