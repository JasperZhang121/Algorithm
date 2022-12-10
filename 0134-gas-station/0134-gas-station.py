class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        total = 0
        minTank = 100000
        minIndex = 0
        
        for i in range(n):
            total += gas[i]-cost[i]
            if total<minTank:
                minTank = total
                minIndex = i
        
        return -1 if total<0 else (minIndex+1)%n
                