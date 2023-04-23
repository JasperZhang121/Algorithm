### Convert Function

```python
    def convert(self, n,x):
        tem=""
        while n>1:
            tem+=str(n%x)
            if n//x in range(0,x):
                tem+=str(n//x)
            n//=x
        return tem
```
This code defines a function convert that takes two arguments n and x. It returns a string that represents the base-x representation of the integer n. The function converts n to base-x by repeatedly dividing n by x, appending the remainder to a string tem, and continuing until n becomes 1 or less. If n divided by x is within the range from 0 to x-1, the quotient is also appended to the tem string. The resulting tem string represents the base-x representation of the original integer n.

