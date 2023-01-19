class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # frequency table to store the frequency of the remainder
        remainderFrq = defaultdict(int)
        # Empty sub array will have a sum of 0 and remainder of 0, thus the frequency of 0 is 1 before we go into the array
        remainderFrq[0] = 1
        
        res = prefixSum = 0
        for n in nums:
            prefixSum += n
            remainder = prefixSum % k
            res += remainderFrq[remainder]
            remainderFrq[remainder] += 1
        return res
        