class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        a,b= [],[]
        c = 0
        for i in range(len(nums)):
            if nums[i]==1:
                a.append(1)
                nums[i] = -1
                c+=1
            if nums[i]==2:
                b.append(2)
                nums[i] = -1
                c+=1

        nums += a
        nums += b

        while c>0:
            nums.remove(-1)
            c-=1
        
