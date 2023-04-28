Loop and sort would be the most intuitive method.

However, you can also use the two pointers to solve the question, which is quite elegant from my opinion:


```python

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
```


