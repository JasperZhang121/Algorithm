Track current min and max.

Update the min, 
then evreytime meet a new stock price calculate whether the subtract value larger than current max.

The reason is simple:
- we want to the difference between lowest and highest
- the new min value does not influence our current max based on previous calculation
- the new min then used for future calculations of current max
