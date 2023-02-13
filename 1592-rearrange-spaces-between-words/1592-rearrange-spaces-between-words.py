class Solution:
    def reorderSpaces(self, text: str) -> str:
                
        
        spaces,words,tmp = 0,[], ""
        
        for x in text:
            if x == ' ':
                spaces+=1
                if tmp != "":
                    words.append(tmp)
                    tmp = ""
            else:
                tmp+=x
        
        if tmp !="":
            words.append(tmp)
        
        
        if len(words)==1:
            return words[0]+spaces*" "
    
        divide = spaces//(len(words)-1)
        modulo = spaces%(len(words)-1)
        
        div,mod = " "*divide, " "*modulo
        
        
    
        return div.join(words)+mod
                