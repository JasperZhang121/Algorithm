### Recursion method
Works but too slow to pass all tests.
​
```python
class Solution:
def getRow(self, rowIndex: int) -> List[int]:
n = rowIndex
if n == 0:
return [1]
elif n == 1:
return [1,1]
else:
temp = [0]*(n+1)
temp[0]=temp[-1]=1
for i in range(1,len(temp)-1):
temp[i] = self.getRow(n-1)[i-1]+self.getRow(n-1)[i]
return temp
```