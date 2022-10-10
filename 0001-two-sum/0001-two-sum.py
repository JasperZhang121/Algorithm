class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        i=0
        for x in nums:
            mapp[i] = x
            if target-x in mapp.values():
                for z,w in mapp.items():
                    if w == target-x and i!=z:
                        return [z,i]
            i+=1     