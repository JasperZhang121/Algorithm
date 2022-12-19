class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        a = sorted(nums)
        arr = {}
        arr[a[0]] = 1
        
        for i in range (1,len(a)):
            if a[i]==a[i-1]:
                arr[a[i]]+=1
            else:
                arr[a[i]] = 1
        
        y = sorted(arr.values())[::-1]
        y = y[:k]
        res = []
        
        for x, z in arr.items():
            if z in y:
                res.append(x)
            
        return res