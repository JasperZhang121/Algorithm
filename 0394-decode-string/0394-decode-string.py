class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
                
            else:
                subStr = ''
                while stack[-1] != '[':
                    subStr = stack.pop() + subStr
                stack.pop()
                
                digit = ''
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                    
                stack.append(int(digit) * subStr)
                
        return ''.join(stack)
            
            