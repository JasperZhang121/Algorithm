### Brute Force - Time exceed
​
``` python
class Solution:
def maxOperations(self, nums: List[int], k: int) -> int:
copy = nums[::]
count = 0
for x in nums:
if x in copy and (k-x) in copy:
copy.remove(x)
if (k-x) in copy:
copy.remove((k-x))
count+=1
else:
copy.append(x)
return count
```
​
### -> Hash map for saving time
​