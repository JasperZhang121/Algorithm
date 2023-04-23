class Solution:
    def compress(self, chars: List[str]) -> int:

        n, ptr, cnt = len(chars), 0, 1
        
        for i in range(1,n+1):
            
            # If the current character is the same as the previous one, increment the count
            if i < n and chars[i] == chars[i-1]: cnt += 1
            
             # If the current character is different from the previous one, write the previous character and its count to the list
            else:
                chars[ptr] = chars[i-1]
                ptr+= 1

                if cnt > 1:
                    s = str(cnt)
                    m = len(s)
                    chars[ptr : ptr + m] = s
                    ptr+= m
 
                cnt = 1

        return ptr
                    
                    