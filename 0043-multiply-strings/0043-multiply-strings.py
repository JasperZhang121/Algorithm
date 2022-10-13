class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        res  = [0]*(len(num1)+len(num2))
        for i in range(len(num1))[::-1]:
            carry = 0
            for j in range(len(num2))[::-1]:
                temp = int(num1[i]) * int(num2[j])+carry
                carry, res[i+j+1] = divmod((res[i+j+1]+temp),10)              
            res[i] += carry

        res = "".join(map(str,res))
        res = res.lstrip('0')
        return '0' if not res else res