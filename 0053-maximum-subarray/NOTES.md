# Use dp for solving
### Each pos in dp array:
- is the max number at that position we can get from any possible combination of previous subarrys even it decreases, but it is the max in that position
### Explain:
- if the current number > previous sub array + current number (meaning previous is negative), we record the current number meaning start a new array
- else the current number < previous sub array + current number (the max number we can get so far at this positon even it decreases), record the sum