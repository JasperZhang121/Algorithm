class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        lis = [char for char in tiles]
        memo = set()
        c = 0
        
        def bt(current, remain):
            if current!=[]:
                t = "".join(current)
                if t not in memo:
                    memo.add(t)
                    nonlocal c
                    c+=1       
            
            for x in remain:
                current.append(x)
                temp = remain[::]
                temp.remove(x)
                bt(current,temp)
                current.pop()
        
        bt([],lis)
        return c