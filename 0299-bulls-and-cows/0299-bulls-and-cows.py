class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        h = Counter(secret)
            
        bulls = cows = 0
        for idx, ch in enumerate(guess):
            if ch in h:
                # corresponding characters match
                if ch == secret[idx]:
                    # update the bulls
                    bulls += 1
                    # update the cows 
                    # if all ch characters from secret 
                    # were used up
                    cows -= int(h[ch] <= 0)
                # corresponding characters don't match
                else:
                    # update the cows
                    cows += int(h[ch] > 0)
                # ch character was used
                h[ch] -= 1
                
        return "{}A{}B".format(bulls, cows)
                
            
    
                    
        