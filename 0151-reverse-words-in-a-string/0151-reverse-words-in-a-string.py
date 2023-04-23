class Solution:
    def reverseWords(self, s: str) -> str:
        
        word, temp, prefix  = True, [], ""
        
        for x in s:
            if x != " ":
                prefix += x
            else:
                if prefix != "":
                    temp.append(prefix)
                    prefix = ""
        
        if prefix!="":
            temp.append(prefix)
        
        temp.reverse()
        
        return " ".join(temp)
                
                
                
        