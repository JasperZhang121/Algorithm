class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels,res = [],""
        
        for l in s:
            if l in "aeiouAEIOU":
                vowels.append(l)
        
        pointer = len(vowels)-1
        
        for l in s:
            if l not in "aeiouAEIOU":
                res+=l
            else:
                res+=vowels[pointer]
                pointer-=1
                
        return res
                